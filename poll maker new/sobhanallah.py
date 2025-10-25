from login import Login

class Poll:
    def __init__(self, name, owner, pollID, mode, list_op) -> None:
        self.name = name
        self.id = pollID
        self.owner = owner
        self.list_op = list_op
        self.mode =mode 

    def show(self):
        print("##########################")
        print("Name:", self.name)
        i = 1
        for x in self.list_op:
            print( "option " + str(i) + ": " + x)
            i += 1
        print("##########################")


class Ray:
    def __init__(self, id, option) -> None:
        self.id = id
        self.option = option

class cuserid:
    def __init__(self, id, cuser) -> None:
        self.id = id
        self.user = cuser


class Runner:
    def __init__(self):

        self.polls = list()
        self.rays = list()
        self.per = list()
        self.lastID = 0
        self.load()
        self.loginSystem = Login()
        self.currentuser = self.loginSystem.run()
        self.run()

    def load(self):
        ####### Load Polls ###########
        try:
            f = open("PollDB.txt", mode="r")
            lines = f.readlines()
            self.lastID = int(lines[0])
        except:
            f = open("PollDB.txt", mode="w")
            lines = list()

        for p in lines[1:]:
            tmp = p.strip().split(" ")
            list_op = []
            for i in tmp[4:]:
                list_op.append(i)
            self.polls.append(Poll(tmp[0], tmp[1], tmp[2], tmp[3], list_op))
        ######## Load Rays ##########
        try:
            f = open("RayDB.txt", mode="r")
            lines = f.readlines()
        except:
            f = open("RayDB.txt", mode="w")
            lines = list()

        for r in lines:
            tmp = r.split(" ")
            self.rays.append(Ray(tmp[0], tmp[1]))
        ######## Load Person ##########
        try:
            f = open("PerDB.txt", mode="r")
            lines = f.readlines()
        except:
            f = open("PerDB.txt", mode="w")
            lines = list()

        for r in lines:
            tmp = r.split(" ")
            self.per.append(cuserid(tmp[0], tmp[1]))

    def save(self):
        ####### Save Polls ###########
        f = open("PollDB.txt", mode="w")
        f.write(str(self.lastID)+"\n")
        for p in self.polls:
            toWrite = p.name+" "+p.owner+" "+str(p.id)+" "+p.mode
            for l in p.list_op:
                toWrite += " "+l
            f.write(toWrite)
            f.write("\n")

        ######## Save Rays ##########
        f = open("RayDB.txt", mode="w")
        for r in self.rays:
            toWrite = r.id + " " + r.option + "\n"
            f.write(toWrite)

        ######## Save Pers ##########
        f = open("PerDB.txt", mode="w")
        for r in self.per:
            toWrite = r.id + " " + r.cuser + "\n"
            f.write(toWrite)

    def participate(self, pollID):
        for poll in self.polls:
            if poll.id == pollID:
                if str(poll.mode) == "active" :
                    poll.show()
                    selOp = None
                    while not selOp in poll.list_op:
                        selOp = input("Please select an option: ").strip()
                        if selOp in poll.list_op:
                            print("Vote submitted")
                            self.rays.append(Ray(pollID, selOp))
                else :
                    print("The selected poll is not active")

    def printPolls(self):
        for p in self.polls:
            print( p.id , ": " , p.name)

    def youpoll(self):
        for p in self.polls:
            print( str(p.id) , ": " , str(p.name),"( ", str(p.mode) ,")")

    def deletpoll(self):
        idToDelete = int(input("Enter id: "))
        for x in self.polls :
            if x[3] == idToDelete :
                if self.currentuser == x[1]:
                    self.polls.remove(x)
                    print("Deleted!")
                else :
                    print("Id not found or you do not have the permission to delete this poll")

    def activstion(self):
        idtoactive = int(input("Enter id: "))
        for x in self.polls :
            if x[2] == idtoactive :
                if self.currentuser == x[1]:
                    if x[3] == "active" :
                        x[3] = "deactive"
                    elif x[3] == "deactive":
                        x[3] = "active"
                else :
                    print("Id not found or you do not have the permission to active or deactive this poll")

    def pollres(self):
        idtores =int(input("Enter id: "))
        for x in self.polls :
            if x[2] == idtores :
                for i in x[4]:
                    temp = 0
                    for y in self.ryas :
                        if y[0] == idtores and y[1] == i :
                            temp +=1
                    print ("There is " + temp + " vote for " + str(i))

    def printRays(self):
        for r in self.rays:
            print("id of poll: " + r.id + " selected option :"+ r.option)

    def run(self):
        while True:
            kar = 0
            print('''1. Create a poll
2. View the polls
3. Participate in a poll
4. View number of participants
5. Delete your poll
6. Activate or deactivate your poll
7. Poll results
8. List of your polls
9. Log out
10. Quit''')
            while kar < 1 or kar > 10:
                kar = int(input("Please enter an option: "))
            if kar == 1:
                name = input("Poll name: ")
                modee = "active"
                op = int(input("How many option: "))
                list_op = []
                for i in range(op):
                    a = input("Option #"+str(i+1)+": ")
                    list_op.append(a)
                p = Poll(name,self.currentuser, self.lastID, modee, list_op)
                self.lastID += 1
                self.polls.append(p)
                print("POll successfully created! ")
                p.show()
            elif kar == 2:
                self.printPolls()
            elif kar == 3:
                boolian =True
                pollIDToPar = input(
                    "Please enter the id of poll you want to participate: ")
                for x in self.per :
                    if x[0] == pollIDToPar :
                        if self.currentuser == x[1] :
                            print("You are already participate in this poll !")
                            boolian = False
                if boolian == True :
                    self.participate(pollIDToPar)
            elif kar == 4:
                self.printRays()
            elif kar == 5:
                self.deletpoll()
            elif kar == 6:
                self.activstion()
            elif kar == 7:
                self.pollres()
            elif kar == 8:
                self.youpoll()
            elif kar == 9:
                self.currentuser =None
                self.currentuser = self.loginSystem.run()
            elif kar == 10:
                self.save()
                self.loginSystem.save()
                break
r = Runner()