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
