import os
from datetime import datetime
from Class import Estate
from Class import Admin
from Class import seller
from Class import Home
from Class import message
from Class import Want
#log_file tamam car ha ro tosh zachire mi konim hata zaman ejra
os.chdir(os.path.dirname(os.path.realpath(__file__)))
log_file=open(str(os.getcwd())+"\\log.txt","a+")
log_file.write( "************************************"+str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+" App Opened\n")
log_file.close()


e=Estate()
print(e.LoadAdmins())
print(e.LoadSeller())
print(e.LoadHomes())
print(e.LoadWants())
print(e.LoadMessages())
# e.CheckEnables()
#a=Admin(LastCode_Admin,"Ali2","1385,3,28","004384928174",["22222222","3332344342"],True,"Admin000","1234",10)
#print(e.AdAdmin(a))
#b=Admin(LastCode_Admin,"Ali2","1385,3,28","004384928175",["22222222","3332344342"],True,"Admin000","1234",10)
#print(e.ChangeAdmin(b,"Ali2",1))
#print(e.admins[1].name)
print('''Hello there!
Wellcome to Kordi estate:[connect us:02144444444, Iran Tehran Azadi No121]
( For help write "/help" )
''')
ouruser=None
typeouruser=0
while True:
    LastCode_Admin=1
    LastCode_Home=1
    LastCode_Seller=1
    LastCode_Want=1
    LastCode_Messages=1
    try:
        if(os.path.isfile(str(os.getcwd())+"\\Varibs.txt")):
            va=open(str(os.getcwd())+"\\Varibs.txt","r")
            var=va.readlines()
            va.close()
            LastCode_Admin=int(var[0])
            LastCode_Home=int(var[1])
            LastCode_Seller=int(var[2])
            LastCode_Want=int(var[3])
            LastCode_Messages=int(var[4])
        else:
            nva=open(str(os.getcwd())+"\\Varibs.txt","a+")
            nva.write("1\n")
            nva.write("1\n")
            nva.write("1\n")
            nva.write("1\n")
            nva.write("1\n")
            nva.close()
            LastCode_Admin=1
            LastCode_Home=1
            LastCode_Seller=1
            LastCode_Want=1
            LastCode_Messages=1
    except:
        print("Error in line 9 [varibs loading]")
    finally:
        try:
            nva.close()
            va.close()
        except:
            ""
    command=input()
    
    if command=="/help":
        print('''/log in : log in men!
/log out : log out it is eazy
/sign up : Hello customer!sign up...
/ad admin : if you logged in and you are admin you can ad new admin
/change me : change your pass or other informations
/Wants : Are you admin? if you are you can see all requests:)
/Customers : Are you admin? if...... you can see all customers
/Homes : Show all home that are availble
/my homes : Show all homes that you are the owner
/my wants : Show all requests that you worte them before
/accept want : Enter the code of request that is for your home
/write request : Sent new request to buy home!
/search : Search home!
/ad home : Do you have home? Ok upload your home information and sell it!
/me : Show your info!''')
    elif command=="/log in":
        if ouruser==None:
            usear =(input("Username: "))
            passw =(input("Password: ")) 
            tempuser=e.FindAdmin(usear,4)
            tempuser1=e.FindSeller(usear,4)
            if tempuser[0]==True and tempuser[1].password==passw:
                print("Logged in! ")
                ouruser=tempuser[1]
                typeouruser=1
            elif tempuser1[0]==True and tempuser1[1].password==passw:
                print("Logged in! ")
                ouruser=tempuser1[1]
                typeouruser=2
                for i in e.messages:
                    if i.to==ouruser.code:
                        print(i.s)
                        e.RemoveMessage(i)
            else :
                print("Username or password is incorrect!")
        else:
            print("Please first log out with command:[/log out]  !!!")
    elif command=="/log out" and ouruser!=None:
        ouruser=None
        typeouruser=0
        print("Ok Good bye!!!")
    elif command=="/sign up" :
        Name=str(input("What is your name ? "))
        BrithDay=str(input("When is your BrithDay ? [year(2000),month(01),day(01)] "))
        NationalCode=str(input("What is your NationalCode ? "))
        Phones=list(input("What are your Phones ? [Write list of your phones with separator Space] ").split())
        Marrid=True if input("are you married ? [yes/no] ")=="yes" else False
        UserName=str(input("What is your UserName ? "))
        Password=str(input("What is your Password ? "))
        temp=seller(LastCode_Seller,Name,BrithDay,NationalCode,Phones,Marrid,UserName,Password)
        if e.AdSeller(temp)==True :
            print("Welcome! ")
            ouruser=temp    
            typeouruser=2
            for i in e.messages:
                if i.to==ouruser.code:
                    print(i.s)
                    e.RemoveMessage(i)
    elif command=="/ad admin" and typeouruser==1:
        Name=str(input("What is his name ? "))
        BrithDay=str(input("When is his BrithDay ? [year(2000),month(01),day(01)] "))
        NationalCode=str(input("What is his NationalCode ? "))
        Phones=list(input("What is his Phones ? [Write list of your phones with separator Space] ").split())
        Marrid=True if input("is he married ? [yes/no] ")=="yes" else False
        Sabeghe=int(input("How many year did he work ? "))
        UserName=str(input("What is his UserName ? "))
        Password=str(input("What is his Password ? "))
        temp=Admin(LastCode_Admin,Name,BrithDay,NationalCode,Phones,Marrid,UserName,Password,Sabeghe)
        if e.AdAdmin(temp)==True :
            print("Added:)")
    elif command=="/change me":
        if typeouruser==1:
            command=input("Which one? [if you don't want change write NOCHANGE]")
            Name=str(input("What is your name ? "))
            BrithDay=str(input("When is your BrithDay ? [year(2000),month(01),day(01)] "))
            NationalCode=str(input("What is your NationalCode ? "))
            Phones=list(input("What are your Phones ? [Write list of your phones with separator Space] ").split())
            Marrid=True if input("are you married ? [yes/no] ")=="yes" else False
            Sabeghe=int(input("How many year did you work ? "))
            UserName=str(input("What is your UserName ? "))
            Password=str(input("What is your Password ? "))
            if Name=="NOCHANGE":
                Name=ouruser.name
            if BrithDay=="NOCHANGE":
                BrithDay=ouruser.brithday
            if NationalCode=="NOCHANGE":
                NationalCode=ouruser.nationalcode
            if Phones=="NOCHANGE":
                Phones=ouruser.phones
            if Marrid=="NOCHANGE":
                Marrid=ouruser.marrid
            if Sabeghe=="NOCHANGE":
                Sabeghe=ouruser.workyear
            if UserName=="NOCHANGE":
                UserName=ouruser.username
            if Password=="NOCHANGE":
                Password=ouruser.password
            temp=Admin(ouruser.code,Name,BrithDay,NationalCode,Phones,Marrid,UserName,Password,Sabeghe)
            if e.ChangeAdmin(temp,ouruser.code,3)==True :
                print("Changed:)")
                ouruser=e.FindAdmin(ouruser.code,3)[1]
        elif typeouruser==2:
            command=input("Which one? [if you don't want change write NOCHANGE]")
            Name=str(input("What is your name ? "))
            BrithDay=str(input("When is your BrithDay ? [year(2000),month(01),day(01)] "))
            NationalCode=str(input("What is your NationalCode ? "))
            Phones=list(input("What are your Phones ? [Write list of your phones with separator Space] ").split())
            Marrid=True if input("are you married ? [yes/no] ")=="yes" else False
            UserName=str(input("What is your UserName ? "))
            Password=str(input("What is your Password ? "))
            if Name=="NOCHANGE":
                Name=ouruser.name
            if BrithDay=="NOCHANGE":
                BrithDay=ouruser.birthday
            if NationalCode=="NOCHANGE":
                NationalCode=ouruser.nationalcode
            if Phones==["NOCHANGE"]:
                Phones=ouruser.phones
            if Marrid=="NOCHANGE":
                Marrid=ouruser.marrid
            if UserName=="NOCHANGE":
                UserName=ouruser.username
            if Password=="NOCHANGE":
                Password=ouruser.password
            temp=seller(ouruser.code,Name,BrithDay,NationalCode,Phones,Marrid,UserName,Password)
            if e.ChangeSeller(temp,ouruser.code,3)==True :
                print("Changed:)")
                ouruser=e.FindSeller(ouruser.code,3)[1]
    elif command=="/Wants" and typeouruser==1:
        for i in e.wants:
            print(Want.p(i,e))
    elif command=="/Customers" and typeouruser==1:
        for i in e.sellers:
            print(i)
    elif command=="/Homes":
        if typeouruser==1:
            for i in e.homes:
                print(Home.p(i,e))
        elif typeouruser==2:
            for i in e.homes:
                if i.enable:
                    print(Home.p(i,e))
    elif command=="/my homes" and typeouruser==2:
        for i in e.homes:
            if i.owner==ouruser.code:
                print("__________________________Home________________________________")
                print(Home.p(i,e))
                print("______________________requests__________________________")
                for j in e.wants:
                    if j.target==i.code:
                        print(Want.p(j,e))
                        print("______________________________________________________")
    elif command=="/my wants" and typeouruser==2:
        for i in e.wants:
            if i.owner==ouruser.code:
                print("__________________________Want________________________________")
                print(Want.p(i,e))

    elif command=="/accept want":
        if typeouruser==2:
            command=int(input("Want id:"))
            xxx=None
            xxxhome=None
            for i in e.homes:
                if i.owner==ouruser.code:
                    t=False
                    for j in e.wants:
                        if j.target==i.code:
                            if command==j.code:
                                xxx=j
                                xxxhome=i
                                t=True
                                break
                    if t:
                        break
            print(Want.p(xxx,e))
            command=True if input("Are you sure? [yes/no] ")=="yes" else False
            if command:
                if xxx.kind==1:
                    e.RemoveWant(xxx)
                    e.RemoveHome(xxxhome)
                    e.AdMessage(message(LastCode_Messages,xxx.owner,f"salam dadash darkhasti ke dadi ghabol shod mobarak bashe haji:)[{xxx.code}] address khone jadid shoam:{xxxhome.address}"))
                    print("Finish")
                else:
                    
                    e.RemoveWant(xxx)
                    e.RemoveHome(xxxhome)
                    e.AdMessage(message(LastCode_Messages,xxx.owner,f"salam dadash darkhasti ke dadi ghabol shod mobarak bashe haji:)[{xxx.code}] address khone jadid shoam:{xxxhome.address} ejare ta:{xxx.date}"))
                    print("Finish")
    elif command=="/write request" and typeouruser==2:
        try:
            Date=None
            tt=False
            Kind=int(input("What kind do you want to request ? [Purchase: 1 Mortgage: 2]"))
            if Kind!=1:
                Date=datetime.strptime(input("Rent or mortgage for how long ? [For example: 22//10/12 09:15:32 year/month/day hour:min:sec]"), '%y/%m/%d %H:%M:%S')
                tt=True
            elif Kind==1:
                tt=True
            else:
                print("Error Kind shoud be [Purchase: 1 Mortgage: 2]")
            if tt:
                home=int(input("What is your desired home code ? "))
                tt=False
                if e.FindHome(home,2)[0]:
                    if e.FindHome(home,2)[1].mor!=Kind:
                        tt=True
                if tt:
                    temp=Want(LastCode_Want,ouruser.code,Kind,Date,True,home)
                    if e.AdWant(temp)==True :
                        print("Added:)")
                else:
                    print("NO Home with your code!")
        except:
            print("Inputs error!")
    elif command=="/search":
        print("Write Your Filters. If you don't have write skip")
        big=input("How big ? ")
        room=input("With how many room ?")
        moble=input("Moble ? [yes/no] ")
        cell=input("which area ? ")
        mor=input("Ejare? ya frosh kame? [1:ejare,2:frosh] ")
        price1="skip"
        price2="skip"
        if(mor!="skip" and int(mor)==1):
            price1=input("hadaksar rahn: ")
            price2=input("hadaksar ejare: ")
        elif(mor!="skip"):
            price1=input("max price: ")
            price2=10000
        for i in e.homes:
            if i.enable:
                if mor!="skip" and i.mor!=int(mor):
                    continue
                if price1!="skip" and i.price1>int(price1):
                    continue
                if price2!="skip" and i.price2>int(price2):
                    continue
                if big!="skip"and i.big!=int(big):
                    continue
                if room!="skip" and i.room!=int(room):
                    continue
                if moble!="skip" and i.moble!=bool(moble):
                    continue
                if cell!="skip" and i.cell!=int(cell):
                    continue
                print("_________________________________")
                print(Home.p(i,e))
    elif command=="/ad home" and typeouruser==2:
        Kind=str(input("What kind is it ? "))
        Big=int(input("What is the size ? "))
        Room=int(input("With how many room ? "))
        Address=str(input("Address: "))
        important=int(input("How much more money do you pay to sell sooner ? "))
        Cell=str(input("mantaghe ? "))
        moble=True if str(input("Is moble ? [yes/no]"))=="yes" else False
        mor=int(input("Ejare ya Frosh kamel?[1:ejare 2:frosh] "))
        temp=None
        if(mor==1):
            price1=int(input("Rahn: "))
            price2=int(input("Ejare: "))
            temp=Home(LastCode_Home,ouruser.code,Kind,Big,Room,Address,important,Cell,moble,True,price1,price2,mor)
        else:
            price1=int(input("price: "))
            temp=Home(LastCode_Home,ouruser.code,Kind,Big,Room,Address,important,Cell,moble,True,price1,0,2)
        if e.AdHome(temp)==True :
            print("Added:)")
    elif command=="/me" and typeouruser==2:
        print("You are......")
        print("Name:"+str(ouruser.name))
        print("Brithday:"+str(ouruser.birthday))
        print("National code:"+str(ouruser.nationalcode))
        print("Phones:")
        for i in ouruser.phones:
            print(str(i))
        print("Married:"+str(ouruser.marrid))
        print("UserName:"+str(ouruser.username))
        print("Password:******")
    else:
        print("For help write \"/help\"")
try:
    log_file.close()
except:
    ""