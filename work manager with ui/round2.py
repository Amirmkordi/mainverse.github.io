import os
import fun
import re
import datetime
import random
from admin import *
# from kavenegar import *
os.chdir(os.path.dirname(__file__))

class todoo:
    def __init__(self):
        self.file = file = open('data.txt', 'a')
        b = 0
        self.data = [None]*sum(1 for line in open('data.txt', 'r'))
        for i in range(sum(1 for line in open('data.txt', 'r'))):
            self.data[i] = open('data.txt', 'r').readlines()[i].split('|')
        self.data.pop(0)
        max = 0
        for i in range(len(self.data)):
            if int(self.data[i][0]) > max :max = int(self.data[i][0])
        self.id = max
    def SMS(self):
        self.rand = random.randint(10000, 99999)
        print(self.rand)
        # try:
        #     api = KavenegarAPI('664446466A64474375567158344D504931593352666E5A5734487734763936493274546E343745747570773D' )
        #     params = {
        #         'receptor': str(self.number),
        #         'template': 'Cna',
        #         'token': str(self.rand),
        #         'token2': str(self.user),
        #         'type': 'sms',
        #     }   
        #     response = api.verify_lookup(params)
        # except APIException as e: 
        #     print(e)
        # except HTTPException as e: 
        #     print(e)
    def check_sms(self,code,send):
        if send == code:
            return [self.idp,self.idp]
        else:
            return[False,'The entered code is not correct Try agine ']
    def login(self,user,Pass):
        P = admin.login(user, Pass)
        if P[0] == True:
            self.idp = P[1][0]
            self.number = P[1][2]
            self.user = P[1][1]
            self.SMS()
            return[self.rand,'please enter the code that was sent to your number']
            # self.SMS()
        else:
            if P[1] == 'PASS':
                return[False,' Your password is Fals ! Try agine ']
            if P[1] == 'USER':
                return[False,' Your User Name is False ! Try agine ']
    def mobile_check(self,phone):
        if re.fullmatch(r"(09|\+98|00989)[0-9]{9}", phone):return True
        else:return False
    def passcheck(self,passwd):
            if (re.search(r'[@!?*]', passwd)) and len(passwd) >= 8:return True
            else:return False
    def creat_user(self,user,phone,Pass,repass):
        DATA = []
        DATA.append(user)
        if self.mobile_check(phone) == False:
            return[False,'your Phone number is not true try again']
        else: DATA.append(phone)
        if self.passcheck(Pass) ==False:
            return [False,'your password must have (@!?*) try again']
        if Pass != repass:
            return[False,'passwords are not the same try again']
        else:DATA.append(Pass)
        m = person(DATA)
        return[m,f'user created successfully your ID = {m}']
    def new_task(self,title,detail,deadline,tags,id):
        current_time = datetime.datetime.now()
        date_modified = f'{current_time.date()}-{current_time.hour}-{current_time.minute}'
        self.new = f'{str(self.id+1)}|{title}|{detail}|{date_modified}|{date_modified}|{deadline}|{tags}|{id}|False|'
        file = open('data.txt', 'a')
        file.write(self.new+'\n')
        return[str(self.id+1),f'task created succesfully your ID : {str(self.id+1)}']
    def task_list(self,id=None):
        if id != None:return self.data[id]
        else:return self.data
    def editable(self,id,idp):
        data = None
        for i in range(len(self.data)):
            if self.data[i][0] == str(id):
                data = self.data[i]
        if data == None:return[False,'task do not exist']
        if idp == data[7]:
            return [True,[data[1],data[2],data[5],data[6],data[8]]]
        else:
            return[False,'You do not have access to edit this task']
    def edit(self,id,title,detail,deadline,tag,status,idp):
        a = None
        for i in range(len(self.data)):
            if self.data[i][0] == str(id):
                a = self.data[i]
        if a == None:return[False,'task do not exist']
        if idp == a[7]:
            a[1] = title
            a[2] = detail
            a[5] = deadline
            a[6] = tag
            a[8] = status
            current_time = datetime.datetime.now()
            a[4] = f'{current_time.date()}-{current_time.hour}-{current_time.minute}'
            print(a)
            fun.Change_Data(str(id), 'data.txt', a)
            return[True,'task edited successfully']
        else:
            return[False,'You do not have access to edit this task']
    def keyr(self,data):
        if self.sort_by == 'e': arg = 5
        if self.sort_by == 'u': arg = 4
        if self.sort_by == 'c': arg = 3
        return data[arg]
    def sort(self,sort_by,az):
        self.sort_by = sort_by
        self.data.sort(key=self.keyr,reverse=az)
        return self.data
    def topg(self,data):
        current_time = datetime.datetime.now()
        date_modified = f'{current_time.date()}-{current_time.hour}-{current_time.minute}'
        if data[8] == 'True': return 2
        elif data[8] == 'False':
            if date_modified > data[5]:return -1
            if date_modified < data[5]:return 1
            if date_modified == data[5]:return 0
    def group(self):
        self.data.sort(key=self.topg,reverse=True)
        return self.data
    def tag(self,data):
        return data[0]
    def task_by_tag(self):
        tag_list = self.tag_list()
        data = list()
        for i in range(len(self.data)):
            for item in self.data[i][6].split(","):
                if item in tag_list:
                    data.append([item,self.data[i]])
        data.sort(key=self.tag)
        return data
    def  tag_list(self):
        tag_list = list()
        for i in range(len(self.data)):
            tag_list.extend(self.data[i][6].split(','))
        tag_list.sort(reverse=True)
        return list(set(tag_list))
todo = todoo()
if __name__ == '__main__':
    login = False
    while login == False:
        print('1.login\n2.singup')
        x = input()
        if x == '1':
            user = [False,'aa']
            while user[0] == False:
                user = todo.login(input('user name : '), input('password : '))
                print(user[1])
            sc = [False,'a']
            while sc[0] == False:
                sc = todo.check_sms(input('the code that was sent to your number : '), str(user[0]))
                print(sc[1])
            login = True
        if x == '2':
            user = [False,'aa']
            while user[0] == False:
                user = todo.creat_user(input('user name : '), input('phone number : '), input('password : '), input('password : '))
                print(user[1])
                login = True
    print('1.create new task\n2.edit task\n3.tasks list\n4.sort\n5.group\n6.tasks sort by tags\n7.tags list')
    x = input('what shuld i do ? : ')
    if x == '1':
        title = input('title : ')
        detail = input('detail : ')
        current_time = datetime.datetime.now()
        date_modified = f'{current_time.date()}-{current_time.hour}-{current_time.minute}'
        deadline = input('deadline : (example : 2023-04-30-08-00)')
        tags = input('tags : (example : math,fori)')
        todo.new_task(title, detail, deadline, tags, todo.idp)
    if x == '2':
        ed = [False,'a']
        while ed[0] == False:
            id = int(input('ID : '))
            data = todo.editable(id,todo.idp)
            if data[0] == True:
                print(f'1.title = {data[1][0]}\t2.detail = {data[1][1]}\t3.deadline = {data[1][2]}\t4.tags = {data[1][3]}\t5.Done = {data[1][4]}')
                edit = int(input('what do you want to edit : '))
                change_to = input('change to what ? : ')
                data[1][edit-1] = change_to
                ed = todo.edit(id, data[1][0], data[1][1], data[1][2], data[1][3], data[1][4],todo.idp)
                print(ed[1])
            else:print(data[1])
    if x == '3':
        data = todo.task_list()
        for i in range(len(data)):
            print(f'ID = {data[i][0]}\tTitle = {data[i][1]}\tDetail = {data[i][2]}\tDate Created = {data[i][3]}\tLast Edited = {data[i][4]}\tDeadline = {data[i][5]}\tTags = {data[i][6]}\tDone = {data[i][8]}')
    if x == '4':
        print('sort by e = deadline \tu = last edited\tc = date created')
        sort_by = input('which one? :')
        az = input('reverse ?(a = sooodi d = nozoli) : ')
        if az == 'a':az = True
        if az == 'd':az = False
        data = todo.sort(sort_by,az)
        for i in range(len(data)):
            print(f'ID = {data[i][0]}\tTitle = {data[i][1]}\tDetail = {data[i][2]}\tDate Created = {data[i][3]}\tLast Edited = {data[i][4]}\tDeadline = {data[i][5]}\tTags = {data[i][6]}\tDone = {data[i][8]}')
    if x == '5': 
        data = todo.group()
        for i in range(len(data)):
            print(f'ID = {data[i][0]}\tTitle = {data[i][1]}\tDetail = {data[i][2]}\tDate Created = {data[i][3]}\tLast Edited = {data[i][4]}\tDeadline = {data[i][5]}\tTags = {data[i][6]}\tDone = {data[i][8]}')
    if x == '6':
        data = todo.task_by_tag()
        tag = data[0][0]
        for i in range(len(data)):
            if tag != data[i][0]:
                tag = data[i][0]
                print(f'Tag {tag} :')
            print(f'ID = {data[i][1][0]}\tTitle = {data[i][1][1]}\tDetail = {data[i][1][2]}\tDate Created = {data[i][1][3]}\tLast Edited = {data[i][1][4]}\tDeadline = {data[i][1][5]}\tTags = {data[i][1][6]}\Done = {data[i][1][8]}')
    if x == '7':
        y = todo.tag_list()
        for i in range(len(y)):print(y[i],end='\t')