import os
from datetime import datetime

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

class Estate:
    def __init__(self) -> None:
        self.admins=[]
        self.homes=[]
        self.sellers=[]
        self.wants=[]
        self.messages=[]
    # def CheckEnables(self):
    #     for i in self.wants:
    #         if i.enable==False:
    #             d=i.date
    #             if d.year>=datetime.today().year:
    #                 if d.month>=datetime.today().month:
    #                     if d.day>=datetime.today().day:
    #                         if self.FindHome(i.xxx,2)[0]:
    #                             self.AdMessage(message(LastCode_Messages,i.owner,f"salam dash zaman rahn/ejare tamom shode\n{str(self.FindHome(i.xxx,2)[1])}"))
    #                             self.AdMessage(message(LastCode_Messages,self.FindHome(i.xxx,2)[1].owner,f"salam dash khonat barghast\n{str(self.FindHome(i.xxx,2)[1])}"))
    #                             xxxhome=self.FindHome(i.xxx,2)[1]
    #                             e.ChangeHome(Home(xxxhome.code,xxxhome.owner,xxxhome.kind,xxxhome.big,xxxhome.room,xxxhome.address,xxxhome.important,xxxhome.cell,xxxhome.moble,True),xxxhome.code,2)
    #                             e.RemoveWant(i)

    def LoadAdmins(self) ->str:
        try:
            ad=open(str(os.getcwd())+"\\Admins.txt","r")
            ads=ad.readlines()
            
            for target in ads:
                l=list(target.split("|||"))
                ll=list(l[4].split("$$$"))
                self.admins.append(Admin(int(l[0]),l[1],l[2],l[3],ll,bool(l[5]),l[6],l[7],int(l[8])))
        except:
            log_file=open(str(os.getcwd())+"\\log.txt","a+")
            log_file.write( str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+" Admins loading Error!!!\n")
            log_file.close()
            self.admins=[Admin(1,"You","1111,11,11","000000000",[],False,"A@min1","0000",0)]
            ad1=open(str(os.getcwd())+"\\Admins.txt","a+")
            ad1.write("1|||You|||1111,11,11|||000000000||||||False|||A@min1|||0000|||0\n")
            global LastCode_Want
            global LastCode_Seller
            global LastCode_Home
            global LastCode_Admin
            if(os.path.isfile(str(os.getcwd())+"\\Varibs.txt")):
                va=open(str(os.getcwd())+"\\Varibs.txt","r")
                var=va.readlines()
                va.close()
                os.remove(str(os.getcwd())+"\\Varibs.txt")
                var[0]="2\n"
                nva=open(str(os.getcwd())+"\\Varibs.txt","a+")
                nva.writelines(var)
            else:
                #ناتموم!
                nva=open(str(os.getcwd())+"\\Varibs.txt","a+")
                nva.write("2\n")
                nva.write("1\n")
                nva.write("1\n")
                nva.write("1\n")
                LastCode_Admin=1
                LastCode_Home=1
                LastCode_Seller=1
                LastCode_Want=1
            LastCode_Admin+=1
            try:
                ad1.close()
                va.close()
                nva.close()
            except:
                ""
            return "Admin Loading Error!!!"
        else:
            return "Admins loaded!!!"
        finally:
            try:
                ad.close()
            except:
                ""
    def FindAdmin(self,proper:str,kind:int):
        if kind==1:
            for i in self.admins:
                if i.name==proper:
                    return [True,i]
        elif kind==2:
            for i in self.admins:
                if i.nationalcode==proper:
                    return [True,i]
        elif kind==3:
            for i in self.admins:
                if i.code==proper:
                    return [True,i]
        else:
            for i in self.admins:
                if i.username==proper:
                    return [True,i]
        return [False,0]    
    def AdAdmin(self,xxx) -> bool:
        t=True
        try:
            if self.FindAdmin(xxx.code,3)[0]==False:
                if self.FindAdmin(xxx.name,1)[0]==False:
                    if self.FindAdmin(xxx.nationalcode,2)[0]==False:
                        if self.FindAdmin(xxx.username,4)[0]==False:
                            self.admins.append(xxx)
                            ad=open(str(os.getcwd())+"\\Admins.txt","a+")
                            s=""
                            for target in xxx.phones:
                                s+=target+"$$$"
                            ad.write(f"{str(xxx.code)}|||{xxx.name}|||{xxx.birthday}|||{xxx.nationalcode}|||{s}|||{xxx.marrid}|||{xxx.username}|||{xxx.password}|||{str(xxx.workyear)}|||\n")
                            
                            global LastCode_Admin
                            global LastCode_Home
                            global LastCode_Seller
                            global LastCode_Want
                            global LastCode_Messages
                            #چک کن
                            if(os.path.isfile(str(os.getcwd())+"\\Varibs.txt")):
                                va=open(str(os.getcwd())+"\\Varibs.txt","r")
                                var=va.readlines()
                                va.close()
                                os.remove(str(os.getcwd())+"\\Varibs.txt")
                                var[0]=str(int(var[0])+1)+"\n"
                                nva=open(str(os.getcwd())+"\\Varibs.txt","a+")
                                nva.writelines(var)
                            else:
                                #ناتموم!
                                nva=open(str(os.getcwd())+"\\Varibs.txt","a+")
                                nva.write("2\n")
                                nva.write("1\n")
                                nva.write("1\n")
                                nva.write("1\n")
                                nva.write("1\n")
                                LastCode_Admin=1
                                LastCode_Home=1
                                LastCode_Seller=1
                                LastCode_Want=1
                                LastCode_Messages=1
                            LastCode_Admin+=1
                        else:
                            print("Username is not available")
                            t=False
                    else:
                        print("NationalCode is not available")
                        t=False
                else:
                    print("Name is not available")
                    t=False
            else:
                print("Error in id!!!")
                t=False            

                
        except:
            return False
        else: 
            if t:
                log_file=open(str(os.getcwd())+"\\log.txt","a+")
                log_file.write( str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+f" Admin with id {xxx.code} Added!\n")
                log_file.close()
            return t
        finally: 
            try:
                ad.close()
                va.close()
                nva.close()
            except:
                print("Big error in line 129")
    def ChangeAdmin(self,xxx,proper:str,kind:int):
        temp=self.FindAdmin(proper,kind)
        if temp[0]:
            ttt=False
            temp1=[]
            ads=[]
            try:
                ad=open(str(os.getcwd())+"\\Admins.txt","a+")
                ads=ad.readlines()
                ad.close()
                os.remove(str(os.getcwd())+"\\Admins.txt")
                temp1=self.admins.copy()
                self.admins.remove(temp[1])
                if self.FindAdmin(xxx.code,3)[0]==False:
                    if self.FindAdmin(xxx.name,1)[0]==False:
                        if self.FindAdmin(xxx.nationalcode,2)[0]==False:
                            if self.FindAdmin(xxx.username,4)[0]==False:
                                self.admins.append(xxx)
                                alladmins=self.admins.copy()
                                self.admins.clear()
                                va=open(str(os.getcwd())+"\\Varibs.txt","r")
                                var=va.readlines()
                                va.close()
                                for i in alladmins:
                                    if(self.AdAdmin(i)==False):
                                        ttt=True
                                        break
                                
                            else:
                                print("Username is not available")
                                ttt=True
                        else:
                            print("NationalCode is not available")
                            ttt=True
                    else:
                        print("Name is not available")
                        ttt=True
                else:
                    print("Error in id!!!")
                    ttt=True      
            finally:
                try:
                    ad.close()
                finally:
                    global LastCode_Admin
                    global LastCode_Home
                    global LastCode_Seller
                    global LastCode_Want
                    global LastCode_Messages
                    LastCode_Admin=int(var[0])
                    LastCode_Home=int(var[1])
                    LastCode_Seller=int(var[2])
                    LastCode_Want=int(var[3])
                    LastCode_Messages=int(var[4])
                    os.remove(str(os.getcwd())+"\\Varibs.txt")
                    va=open(str(os.getcwd())+"\\Varibs.txt","r")
                    va.writelines(var)
                    va.close()
                    if ttt:
                        self.admins=temp1
                        os.remove(str(os.getcwd())+"\\Admins.txt")
                        ad=open(str(os.getcwd())+"\\Admins.txt","a+")
                        ad.writelines(ads)
                    else:
                        log_file=open(str(os.getcwd())+"\\log.txt","a+")
                        if kind==1:
                            log_file.write( str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+f" Admin with name {proper} changed!\n")
                        elif kind==2:
                            log_file.write( str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+f" Admin with nationalcode {proper} changed!\n")
                        elif kind==3:
                            log_file.write( str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+f" Admin with id {proper} changed!\n")
                        elif kind==4:
                            log_file.write( str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+f" Admin with username {proper} changed!\n")
                        log_file.close()
                        return True
        return False

    def LoadHomes(self) ->str:
        try:
            ad=open(str(os.getcwd())+"\\Homes.txt","r")
            ads=ad.readlines()
            
            for target in ads:
                l=list(target.split("|||"))
                if self.FindSeller(int(l[1]),3)[0]:
                    self.homes.append(Home(int(l[0]),int(l[1]),l[2],int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7]),bool(l[8]),bool(l[9]),int(l[10]),int(l[11]),int(l[12])))
        except:
            log_file=open(str(os.getcwd())+"\\log.txt","a+")
            log_file.write( str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+" Homes loading Error!!!\n")
            log_file.close()
            open(str(os.getcwd())+"\\Homes.txt","a+").close()
            return "Homes loading Error!!!"
        else:
            return "Homes loaded!!!"
        finally:
            try:
                ad.close()
            except:
                ""
    def FindHome(self,proper,kind):
        if kind==1:
            for i in self.homes:
                if i.address==proper:
                    return [True,i]
            return [False,0]
        else:
            for i in self.homes:
                if i.code==proper:
                    return [True,i]
            return [False,0]
    def AdHome(self,xxx) -> bool:
        t=True
        try:
            if self.FindHome(xxx.code,2)[0]==False:
                if self.FindHome(xxx.address,1)[0]==False:
                    self.homes.append(xxx)
                    ad=open(str(os.getcwd())+"\\Homes.txt","a+")
                    ad.write(f"{xxx.code}|||{str(xxx.owner)}|||{xxx.kind}|||{xxx.big}|||{xxx.room}|||{xxx.address}|||{xxx.important}|||{xxx.cell}|||{xxx.moble}|||{xxx.enable}|||{xxx.price1}|||{xxx.price2}|||{xxx.mor}|||\n")
                    global LastCode_Admin
                    global LastCode_Home
                    global LastCode_Seller
                    global LastCode_Want
                    global LastCode_Messages
                    if(os.path.isfile(str(os.getcwd())+"\\Varibs.txt")):
                        va=open(str(os.getcwd())+"\\Varibs.txt","r")
                        var=va.readlines()
                        va.close()
                        os.remove(str(os.getcwd())+"\\Varibs.txt")
                        var[1]=str(int(var[1])+1)+"\n"
                        nva=open(str(os.getcwd())+"\\Varibs.txt","a+")
                        nva.writelines(var)
                    else:
                        nva=open(str(os.getcwd())+"\\Varibs.txt","a+")
                        nva.write("1\n")
                        nva.write("2\n")
                        nva.write("1\n")
                        nva.write("1\n")
                        nva.write("1\n")
                        LastCode_Home=1
                        LastCode_Admin=1
                        LastCode_Seller=1
                        LastCode_Want=1
                        LastCode_Messages=1
                    LastCode_Home+=1
                else:
                    print("Address is not available")
                    t=False
            else:
                print("Error in id!!!")
                t=False
        except:
            return False
        else: return t
        finally: 
            try:
                ad.close()
                va.close()
                nva.close()
            except:
                print("Big error in line 265")
    # def ChangeHome(self,xxx,proper:str,kind:int):
    #         temp=self.FindHome(proper,kind)
    #         if temp[0]:
    #             va=open(str(os.getcwd())+"\\Varibs.txt","r")
    #             var=va.readlines()
    #             va.close()
    #             ttt=False
    #             temp1=[]
    #             ads=[]
    #             try:
    #                 ad=open(str(os.getcwd())+"\\Homes.txt","a+")
    #                 ads=ad.readlines()
    #                 ad.close()
    #                 os.remove(str(os.getcwd())+"\\Homes.txt")
    #                 temp1=self.homes.copy()
    #                 self.homes.remove(temp[1])
    #                 if self.FindHome(xxx.code,2)==False:
    #                     if self.FindHome(xxx.address,1)[0]==False:
    #                         self.homes.append(xxx)
    #                         allhomes=self.homes.copy()
    #                         self.homes.clear()
                            
    #                         for i in allhomes:
    #                             if(self.AdHome(i)==False):
    #                                 ttt=True
    #                                 break
    #                     else:
    #                         print("Address is not available")
    #                         ttt=True
    #                 else:
    #                     print("Error in id!!!")
    #                     ttt=True
    #             finally:
    #                 try:
    #                     ad.close()
    #                 finally:
    #                     global LastCode_Admin
    #                     global LastCode_Home
    #                     global LastCode_Seller
    #                     global LastCode_Want
    #                     global LastCode_Messages
    #                     LastCode_Admin=int(var[0])
    #                     LastCode_Home=int(var[1])
    #                     LastCode_Seller=int(var[2])
    #                     LastCode_Want=int(var[3])
    #                     LastCode_Messages=int(var[4])
    #                     os.remove(str(os.getcwd())+"\\Varibs.txt")
    #                     va=open(str(os.getcwd())+"\\Varibs.txt","a+")
    #                     va.writelines(var)
    #                     va.close()
    #                     if ttt:
    #                         self.homes=temp1
    #                         os.remove(str(os.getcwd())+"\\Homes.txt")
    #                         ad=open(str(os.getcwd())+"\\Homes.txt","a+")
    #                         ad.writelines(ads)
    #                     else:
    #                         log_file=open(str(os.getcwd())+"\\log.txt","a+")
    #                         if kind==1:
    #                             log_file.write( str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+f" Home with address {proper} changed!\n")
    #                         elif kind==2:
    #                             log_file.write( str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+f" Home with code {proper} changed!\n")
                            
    #                         log_file.close()
    #                         return True
    #         return False
    def RemoveHome(self,xxx):
        temp=self.FindHome(xxx.code,2)
        if temp[0]:
            ttt=False
            temp1=[]
            ads=[]
            try:
                ad=open(str(os.getcwd())+"\\Homes.txt","a+")
                ads=ad.readlines()
                ad.close()
                
                os.remove(str(os.getcwd())+"\\Homes.txt")
                open(str(os.getcwd())+"\\Homes.txt","a+").close()
                temp1=self.homes.copy()
                self.homes.remove(temp[1])
                allhomes=self.homes.copy()
                self.homes.clear()
                va=open(str(os.getcwd())+"\\Varibs.txt","r")
                var=va.readlines()
                va.close()
                for i in allhomes:
                    if(self.AdHome(i)==False):
                        ttt=True
                        break
            finally:
                try:
                    ad.close()
                finally:
                    global LastCode_Admin
                    global LastCode_Home
                    global LastCode_Seller
                    global LastCode_Want
                    global LastCode_Messages
                    LastCode_Admin=int(var[0])
                    LastCode_Home=int(var[1])
                    LastCode_Seller=int(var[2])
                    LastCode_Want=int(var[3])
                    LastCode_Messages=int(var[4])
                    os.remove(str(os.getcwd())+"\\Varibs.txt")
                    va=open(str(os.getcwd())+"\\Varibs.txt","a+")
                    va.writelines(var)
                    va.close()
                    if ttt:
                        self.homes=temp1
                        os.remove(str(os.getcwd())+"\\Homes.txt")
                        ad=open(str(os.getcwd())+"\\Homes.txt","a+")
                        ad.writelines(ads)
                    else:
                        log_file=open(str(os.getcwd())+"\\log.txt","a+")
                        log_file.write( str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+f" Home with code {xxx.code} removed!\n")
                        log_file.close()
                        return True
            return False
        
    def LoadSeller(self):
        try:
            ad=open(str(os.getcwd())+"\\Sellers.txt","r")
            ads=ad.readlines()
            
            for target in ads:
                l=list(target.split("|||"))
                ll=list(l[4].split("$$$"))
                self.sellers.append(seller(int(l[0]),l[1],l[2],l[3],ll,bool(l[5]),l[6],l[7]))
        except:
            log_file=open(str(os.getcwd())+"\\log.txt","a+")
            log_file.write( str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+" Sellers loading Error!!!\n")
            log_file.close()
            open(str(os.getcwd())+"\\Sellers.txt","a+").close()
            return "Sellers loading Error!!!"
        else:
            return "Selllers loaded!!!"
        finally:
            try:
                ad.close()
            except:
                ""
    def FindSeller(self,proper:str,kind:int):
        if kind==1:
            for i in self.sellers:
                if i.name==proper:
                    return [True,i]
        elif kind==2:
            for i in self.sellers:
                if i.nationalcode==proper:
                    return [True,i]
        elif kind==3:
            for i in self.sellers:
                if i.code==proper:
                    return [True,i]
        else:
            for i in self.sellers:
                if i.username==proper:
                    return [True,i]
        return [False,0]    
    def AdSeller(self,xxx) -> bool:
        t=True
        try:
            if self.FindSeller(xxx.code,3)[0]==False:
                if self.FindSeller(xxx.name,1)[0]==False:
                    if self.FindSeller(xxx.nationalcode,2)[0]==False:
                        if self.FindSeller(xxx.username,4)[0]==False:
                            self.sellers.append(xxx)
                            ad=open(str(os.getcwd())+"\\Sellers.txt","a+")
                            s=""
                            for target in xxx.phones:
                                s+=target+"$$$"
                            ad.write(f"{str(xxx.code)}|||{xxx.name}|||{xxx.birthday}|||{xxx.nationalcode}|||{s}|||{xxx.marrid}|||{xxx.username}|||{xxx.password}|||\n")
                            global LastCode_Admin
                            global LastCode_Home
                            global LastCode_Seller
                            global LastCode_Want
                            global LastCode_Messages                            
                            if(os.path.isfile(str(os.getcwd())+"\\Varibs.txt")):
                                va=open(str(os.getcwd())+"\\Varibs.txt","r")
                                var=va.readlines()
                                va.close()
                                os.remove(str(os.getcwd())+"\\Varibs.txt")
                                var[2]=str(int(var[2])+1)+"\n"
                                nva=open(str(os.getcwd())+"\\Varibs.txt","a+")
                                nva.writelines(var)
                                
                            else:
                                nva=open(str(os.getcwd())+"\\Varibs.txt","a+")
                                nva.write("1\n")
                                nva.write("1\n")
                                nva.write("2\n")
                                nva.write("1\n")
                                nva.write("1\n")
                                LastCode_Admin=1
                                LastCode_Home=1
                                LastCode_Seller=1
                                LastCode_Want=1
                                LastCode_Messages=1
                            LastCode_Seller+=1
                        else:
                            print("Username is not available")
                            t=False
                    else:
                        print("NationalCode is not available")
                        t=False
                else:
                    print("Name is not available")
                    t=False
            else:
                print("Error in id!!!")
                t=False            

                
        except:
            return False
        else: 
            if t:
                log_file=open(str(os.getcwd())+"\\log.txt","a+")
                log_file.write( str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+f" Seller with id {xxx.code} Added!\n")
                log_file.close()
            return t
        finally: 
            try:
                ad.close()
                va.close()
                nva.close()
            except:
                ""
    def ChangeSeller(self,xxx,proper:str,kind:int):
        temp=self.FindSeller(proper,kind)
        if temp[0]:
            ttt=False
            temp1=[]
            ads=[]
            try:
                ad=open(str(os.getcwd())+"\\Sellers.txt","a+")
                ads=ad.readlines()
                ad.close()
                os.remove(str(os.getcwd())+"\\Sellers.txt")
                temp1=self.sellers.copy()
                self.sellers.remove(temp[1])
                if self.FindSeller(xxx.code,3)[0]==False:
                    if self.FindSeller(xxx.name,1)[0]==False:
                        if self.FindSeller(xxx.nationalcode,2)[0]==False:
                            if self.FindSeller(xxx.username,4)[0]==False:
                                self.sellers.append(xxx)
                                allsellers=self.sellers.copy()
                                self.sellers.clear()
                                va=open(str(os.getcwd())+"\\Varibs.txt","r")
                                var=va.readlines()
                                va.close()
                                for i in allsellers:
                                    if(self.AdSeller(i)==False):
                                        ttt=True
                                        break
                            else:
                                print("Username is not available")
                                ttt=True
                        else:
                            print("NationalCode is not available")
                            ttt=True
                    else:
                        print("Name is not available")
                        ttt=True
                else:
                    print("Error in id!!!")
                    ttt=True      
            finally:
                try:
                    ad.close()
                finally:
                    global LastCode_Admin
                    global LastCode_Home
                    global LastCode_Seller
                    global LastCode_Want
                    global LastCode_Messages
                    LastCode_Admin=int(var[0])
                    LastCode_Home=int(var[1])
                    LastCode_Seller=int(var[2])
                    LastCode_Want=int(var[3])
                    LastCode_Messages=int(var[4])
                    os.remove(str(os.getcwd())+"\\Varibs.txt")
                    va=open(str(os.getcwd())+"\\Varibs.txt","a+")
                    va.writelines(var)
                    va.close()
                    if ttt:
                        self.sellers=temp1
                        os.remove(str(os.getcwd())+"\\Sellers.txt")
                        ad=open(str(os.getcwd())+"\\Sellers.txt","a+")
                        ad.writelines(ads)
                    else:
                        log_file=open(str(os.getcwd())+"\\log.txt","a+")
                        if kind==1:
                            log_file.write(str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+f" Seller with name {proper} changed!\n")
                        elif kind==2:
                            log_file.write(str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+f" Seller with nationalcode {proper} changed!\n")
                        elif kind==3:
                            log_file.write(str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+f" Seller with id {proper} changed!\n")
                        elif kind==4:
                            log_file.write(str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+f" Seller with username {proper} changed!\n")
                        log_file.close()
                        return True
        return False

    def LoadWants(self) ->str:
        try:
            ad=open(str(os.getcwd())+"\\Wants.txt","r")
            ads=ad.readlines()
            
            for target in ads:
                l=list(target.split("|||"))
                if self.FindSeller(int(l[1]),3)[0]:
                    if self.FindHome(int(l[5]),2)[0]:
                        Date=datetime.strptime(l[3], '%Y-%m-%d %H:%M:%S')
                        self.wants.append(Want(int(l[0]),int(l[1]),int(l[2]),Date,bool(l[4]),int(l[5])))
        except:
            log_file=open(str(os.getcwd())+"\\log.txt","a+")
            log_file.write( str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+" Wants loading Error!!!\n")
            log_file.close()
            open(str(os.getcwd())+"\\Wants.txt","a+").close()
            return "Wants loading Error!!!"
        else:
            return "Wants loaded!!!"
        finally:
            try:
                ad.close()
            except:
                ""
    def FindWant(self,proper,kind):
        if kind==1:
            for i in self.wants:
                if i.code==proper:
                    return [True,i]
            return [False,0]
    def AdWant(self,xxx) -> bool:
        t=True
        try:
            if self.FindWant(xxx.code,1)[0]==False:
                    self.wants.append(xxx)
                    ad=open(str(os.getcwd())+"\\Wants.txt","a+")
                    ad.write(f"{xxx.code}|||{xxx.owner}|||{xxx.kind}|||{xxx.date}|||{xxx.enable}|||{xxx.target}|||\n")
                    global LastCode_Admin
                    global LastCode_Home
                    global LastCode_Seller
                    global LastCode_Want
                    global LastCode_Messages
                    if(os.path.isfile(str(os.getcwd())+"\\Varibs.txt")):
                        va=open(str(os.getcwd())+"\\Varibs.txt","r")
                        var=va.readlines()
                        va.close()
                        os.remove(str(os.getcwd())+"\\Varibs.txt")
                        var[3]=str(int(var[3])+1)+"\n"
                        nva=open(str(os.getcwd())+"\\Varibs.txt","a+")
                        nva.writelines(var)
                    else:
                        nva=open(str(os.getcwd())+"\\Varibs.txt","a+")
                        nva.write("1\n")
                        nva.write("1\n")
                        nva.write("1\n")
                        nva.write("2\n")
                        nva.write("1\n")
                        LastCode_Home=1
                        LastCode_Admin=1
                        LastCode_Seller=1
                        LastCode_Want=1
                        LastCode_Messages=1
                    LastCode_Want+=1
                
            else:
                print("Error in id!!!")
                t=False
        except:
            return False
        else: 
            if t:
                log_file=open(str(os.getcwd())+"\\log.txt","a+")
                log_file.write( str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+f" Want with id {xxx.code} Added!\n")
                log_file.close()
            return t
        finally: 
            try:
                ad.close()
                va.close()
                nva.close()
            except:
                print("Big error in line 265")
    def RemoveWant(self,xxx):
        temp=self.FindWant(xxx.code,1)
        if temp[0]:
            ttt=False
            temp1=[]
            ads=[]
            try:
                ad=open(str(os.getcwd())+"\\Wants.txt","a+")
                ads=ad.readlines()
                ad.close()
                os.remove(str(os.getcwd())+"\\Wants.txt")
                open(str(os.getcwd())+"\\Wants.txt","a+").close()
                temp1=self.wants.copy()
                self.wants.remove(temp[1])
                allwants=self.wants.copy()
                self.wants.clear()
                va=open(str(os.getcwd())+"\\Varibs.txt","r")
                var=va.readlines()
                va.close()
                for i in allwants:
                    if(self.AdWant(i)==False):
                        ttt=True
                        break
            finally:
                try:
                    ad.close()
                finally:
                    global LastCode_Admin
                    global LastCode_Home
                    global LastCode_Seller
                    global LastCode_Want
                    global LastCode_Messages
                    LastCode_Admin=int(var[0])
                    LastCode_Home=int(var[1])
                    LastCode_Seller=int(var[2])
                    LastCode_Want=int(var[3])
                    LastCode_Messages=int(var[4])
                    os.remove(str(os.getcwd())+"\\Varibs.txt")
                    va=open(str(os.getcwd())+"\\Varibs.txt","a+")
                    va.writelines(var)
                    va.close()
                    if ttt:
                        self.wants=temp1
                        os.remove(str(os.getcwd())+"\\Wants.txt")
                        ad=open(str(os.getcwd())+"\\Wants.txt","a+")
                        ad.writelines(ads)
                    else:
                        log_file=open(str(os.getcwd())+"\\log.txt","a+")
                        log_file.write( str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+f" Want with code {xxx.code} removed!\n")
                        log_file.close()
                        return True
        return False
    # def ChangeWant(self,xxx,proper:str,kind:int):
    #     #kind 1 = code
    #     temp=self.FindWant(proper,kind)
    #     if temp[0]:
    #         ttt=False
    #         temp1=[]
    #         ads=[]
    #         try:
    #             ad=open(str(os.getcwd())+"\\Wants.txt","a+")
    #             ads=ad.readlines()
    #             ad.close()
    #             os.remove(str(os.getcwd())+"\\Wants.txt")
    #             temp1=self.wants.copy()
    #             self.wants.remove(temp[1])
    #             if self.FindWant(xxx.code,1)[0]==False:
    #                 self.wants.append(xxx)
    #                 allwants=self.wants.copy()
    #                 self.wants.clear()
    #                 va=open(str(os.getcwd())+"\\Varibs.txt","r")
    #                 var=va.readlines()
    #                 va.close()
    #                 for i in allwants:
    #                     if(self.AdWant(i)==False):
    #                         ttt=True
    #                         break
    #             else:
    #                 print("Error in id!!!")
    #                 ttt=True         
    #         finally:
    #             try:
    #                 ad.close()
    #             finally:
    #                 global LastCode_Admin
    #                 global LastCode_Home
    #                 global LastCode_Seller
    #                 global LastCode_Want
    #                 global LastCode_Messages
    #                 LastCode_Admin=int(var[0])
    #                 LastCode_Home=int(var[1])
    #                 LastCode_Seller=int(var[2])
    #                 LastCode_Want=int(var[3])
    #                 LastCode_Messages=int(var[4])
    #                 os.remove(str(os.getcwd())+"\\Varibs.txt")
    #                 va=open(str(os.getcwd())+"\\Varibs.txt","r")
    #                 va.writelines(var)
    #                 va.close()
    #                 if ttt:
    #                     self.wants=temp1
    #                     os.remove(str(os.getcwd())+"\\Wants.txt")
    #                     ad=open(str(os.getcwd())+"\\Wants.txt","a+")
    #                     ad.writelines(ads)
    #                 else:
    #                     log_file=open(str(os.getcwd())+"\\log.txt","a+")
    #                     if kind==1:
    #                         log_file.write( str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+f" Want with code {proper} changed!\n")
    #                     log_file.close()
    #                     return True
    #     return False

    def FindMessage(self,proper,kind):
        #kind =1 code   kind=2 owner
        t=False
        l=[]
        if kind==1:
            for i in self.messages:
                if i.code==proper:
                    return [True,i]
        elif kind==2:
            for i in self.messages:
                if i.owner==proper:
                    t=True
                    l.append(i)
        if t:
            return [True,l]
        else:
            return [False,0]
    def LoadMessages(self):
        try:
            ad=open(str(os.getcwd())+"\\Messages.txt","r")
            ads=ad.readlines()
            
            for target in ads:
                l=list(target.split("|||"))
                if self.FindSeller(int(l[1]),3)[0]:
                        self.messages.append(message(int(l[0]),int(l[1]),str(l[2])))
        except:
            log_file=open(str(os.getcwd())+"\\log.txt","a+")
            log_file.write( str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+" Messages loading Error!!!\n")
            log_file.close()
            open(str(os.getcwd())+"\\Messages.txt","a+").close()
            return "Messages loading Error!!!"
        else:
            return "Messages loaded!!!"
        finally:
            try:
                ad.close()
            except:
                ""
    def AdMessage(self,xxx):
        t=True
        try:
            if self.FindMessage(xxx.code,1)[0]==False:
                    self.messages.append(xxx)
                    ad=open(str(os.getcwd())+"\\Messages.txt","a+")
                    ad.write(f"{xxx.code}|||{xxx.to}|||{xxx.s}|||\n")
                    global LastCode_Admin
                    global LastCode_Home
                    global LastCode_Seller
                    global LastCode_Want
                    global LastCode_Messages

                    if(os.path.isfile(str(os.getcwd())+"\\Varibs.txt")):
                        va=open(str(os.getcwd())+"\\Varibs.txt","r")
                        var=va.readlines()
                        va.close()
                        os.remove(str(os.getcwd())+"\\Varibs.txt")
                        var[4]=str(int(var[4])+1)+"\n"
                        nva=open(str(os.getcwd())+"\\Varibs.txt","a+")
                        nva.writelines(var)
                    else:

                        nva=open(str(os.getcwd())+"\\Varibs.txt","a+")
                        nva.write("1\n")
                        nva.write("1\n")
                        nva.write("1\n")
                        nva.write("1\n")
                        nva.write("2\n")
                        LastCode_Home=1
                        LastCode_Admin=1
                        LastCode_Seller=1
                        LastCode_Want=1
                        LastCode_Messages=1
                    LastCode_Messages+=1
                
            else:
                print("Error in id!!!")
                t=False
        except:
            return False
        else: 
            if t:
                log_file=open(str(os.getcwd())+"\\log.txt","a+")
                log_file.write( str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+f" Message with id {xxx.code} Added!\n")
                log_file.close()
            return t
        finally: 
            try:
                ad.close()
                va.close()
                nva.close()
            except:
                print("Big error in line 265")
    def RemoveMessage(self,xxx):
        temp=self.FindMessage(xxx.code,1)
        if temp[0]:
            ttt=False
            temp1=[]
            ads=[]
            try:
                ad=open(str(os.getcwd())+"\\Messages.txt","a+")
                ads=ad.readlines()
                ad.close()
                
                os.remove(str(os.getcwd())+"\\Messages.txt")
                open(str(os.getcwd())+"\\Messages.txt","a+").close()
                temp1=self.messages.copy()
                self.messages.remove(temp[1])
                allmessages=self.messages.copy()
                self.messages.clear()
                va=open(str(os.getcwd())+"\\Varibs.txt","r")
                var=va.readlines()
                va.close()
                for i in allmessages:
                    if(self.AdMessages(i)==False):
                        ttt=True
                        break
            finally:
                try:
                    ad.close()
                finally:
                    global LastCode_Admin
                    global LastCode_Home
                    global LastCode_Seller
                    global LastCode_Want
                    global LastCode_Messages
                    LastCode_Admin=int(var[0])
                    LastCode_Home=int(var[1])
                    LastCode_Seller=int(var[2])
                    LastCode_Want=int(var[3])
                    LastCode_Messages=int(var[4])
                    os.remove(str(os.getcwd())+"\\Varibs.txt")
                    va=open(str(os.getcwd())+"\\Varibs.txt","a+")
                    va.writelines(var)
                    va.close()
                    if ttt:
                        self.messages=temp1
                        os.remove(str(os.getcwd())+"\\Messages.txt")
                        ad=open(str(os.getcwd())+"\\Messages.txt","a+")
                        ad.writelines(ads)
                    else:
                        log_file=open(str(os.getcwd())+"\\log.txt","a+")
                        log_file.write( str(datetime.today())+":"+datetime.now().strftime("%H:%M:%S")+f" Messages with code {xxx.code} removed!\n")
                        log_file.close()
                        return True
        return False

class Human:
    def __init__(self,Name:str,BrithDay:str,NationalCode:str,Phones:list,Marrid:bool) -> None:
        self.name=Name
        self.birthday=BrithDay
        self.nationalcode=NationalCode
        self.phones=Phones
        self.marrid=Marrid

    def CahngeHuman(self,Name:str,BrithDay:str,NationalCode:str,Phones:list,Marrid:bool):
        if(type(Name)==str):
            self.name=Name
        if(type(BrithDay)==str):
            self.birthday=BrithDay
        if(type(NationalCode)==str):
            self.nationalcode=NationalCode
        if(type(Phones)==list):
            self.phones=Phones
        if(type(Marrid)==bool):
            self.marrid=Marrid
class Admin(Human):
    def __init__(self,Codee:int, Name: str, BrithDay: str, NationalCode: str, Phones: list, Marrid: bool,UserName:str,Password:str,Sabeghe:int) -> None:
        super().__init__(Name, BrithDay, NationalCode, Phones, Marrid)
        self.password=Password
        self.username=UserName
        self.workyear=Sabeghe
        self.code=Codee
    def __str__(self) -> str:
        return f"{self.username}  {self.name}"
class seller(Human):
    def __init__(self,Codee:int, Name: str, BrithDay: str, NationalCode: str, Phones: list, Marrid: bool,UserName:str,Password:str) -> None:
        super().__init__(Name, BrithDay, NationalCode, Phones, Marrid)
        self.password=Password
        self.username=UserName
        self.code=Codee
    def __str__(self) -> str:
        return f"{self.username}  {self.name}"
class Home:
    def __init__(self,Codee:int,Owner:int,Kind:str,Big:int,Room:int,Address:str,Important:int,Cell:int,Moble:bool,Enable:bool,price1,price2,mor) -> None: #owner is id of seller 
        #mor1->ejare  mor2->kharid
        self.code=Codee
        self.owner=Owner
        self.enable=Enable
        self.kind=Kind
        self.big=Big
        self.room=Room
        self.address=Address
        self.important=Important
        self.cell=Cell
        self.moble=Moble
        self.price1=price1
        self.price2=price2
        self.mor=mor
    def p(self,e) -> str:
        if(self.mor==1):
            return f'''ID : {self.code}
Owner: {"Not Found!" if e.FindSeller(self.owner,3)==False else str(e.FindSeller(self.owner,3)[1])}
Address: {self.address}
Enable: {self.enable}
Size: {self.big}
Kind: {self.kind}
Rooms: {self.room}
Mantaghe: {self.cell}
Moble: {"Yes" if self.moble else "No"}
Rahn: {self.price1}
Ejare: {self.price2}'''
        else:
            return f'''ID : {self.code}
Owner: {"Not Found!" if e.FindSeller(self.owner,3)==False else str(e.FindSeller(self.owner,3)[1])}
Address: {self.address}
Enable: {self.enable}
Size: {self.big}
Kind: {self.kind}
Rooms: {self.room}
Mantaghe: {self.cell}
Moble: {"Yes" if self.moble else "No"}
Price: {self.price1}'''
    def __lt__(self,other):
        if(self.important<other.important):
            return True
        else:
            return False
    def __gt__(self,other):
        if(self.important>other.important):
            return True
        else:
            return False
    def __ge__(self,other):
        if(self.important>=other.important):
            return True
        else:
            return False
    def __le__(self,other):
        if(self.important<=other.important):
            return True
        else:
            return False
    def __eq__(self,other):
        if(self.important==other.important):
            return True
        else:
            return False
    def __ne__(self,other):
        if(self.important!=other.important):
            return True
        else:
            return False
class Want:
    def __init__(self,Codee:int,Owner:int,Kind:str,Date:datetime,Enable:bool,xxx:int) -> None:
        # kind 1 = buy kind 2 = ejare
        self.code=Codee
        self.owner=Owner
        self.kind=Kind
        self.date=Date
        self.enable=Enable
        self.target=xxx
    def p(self,e) -> str:
        return f'''ID: {self.code}
Owner: {"Not Found!" if e.FindSeller(self.owner,3)==False else str(e.FindSeller(self.owner,3)[1])}
Kind: {self.kind}
Date: {self.date}
Target: {"Not Found!" if e.FindHome(self.target,2)==False else Home.p(e.FindHome(self.target,2)[1],e)}'''
class message:
    def __init__(self,codee:int,to:int,s:str) -> None:
        self.code=codee
        self.to=to
        self.s=s