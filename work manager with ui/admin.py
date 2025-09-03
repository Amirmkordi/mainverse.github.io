import fun
import datetime

ID = datetime.datetime.now().microsecond // 1000

class person:
    def __init__(self, DATA):  # name - family - date - phonnum
        global ID
        self.ID = 'P_' + str(ID)
        DATA.insert(0, self.ID)
        self.DATA = DATA
        fun.add_data(self.DATA, "dataPerson.txt")

    def show_H(ID):  # show data of homes
        listOfdata = []
        for i in range(fun.count("dataMelk.txt")):
            y = open('dataMelk.txt', "r").readlines()[i].split("|")
            if y[2] == ID or y[1] == ID:
                listOfdata.append(y)
        return (listOfdata)

    def show_R(ID):  # show data of requests
        listOfdata = []
        for i in range(fun.count('dataRequest.txt')):
            y = open('dataRequest.txt', "r").readlines()[i].split("|")
            if y[2] == ID:
                listOfdata.append(y)
        return (listOfdata)

    def __str__(self) -> str:
        return self.ID

class admin:

    def __init__(self, data):  # name , family , user , pass
        self.ID = 'A_' + str(ID)
        data.insert(0, self.ID)
        self.DATA = data
        fun.add_data(self.DATA, "dataPerson.txt")

    def login(USER, PASS):
        P = fun.find(USER, 1, 'dataPerson.txt')
        if P:
            if P[1][3] == PASS:
                return [True, P[1]]
            else:
                return [False, 'PASS']
        else:
            return [False, 'USER']
