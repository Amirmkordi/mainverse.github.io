import os

def listToString(s, split):
    listToStr = split.join([str(elem) for i, elem in enumerate(s)])
    return (listToStr)

def stri(Data):  # str
    m = ''
    for i in range(len(Data)):
        if Data[i] == '\n' or (i == len(Data) - 1 and Data[i] == ''):
            m += Data[i]
        else :
            m += str(Data[i])+'|'
    return (m)


def add_data(data, file):  # add data in file
    f = open(file, "a")
    f.write('\n')
    f.write(stri(data))
    f.close


def show_Data(file): # return your data
    listOfdata=[None]*sum(1 for line in open(file, 'r'))
    for i in range(sum(1 for line in open(file, 'r'))):
        listOfdata[i] = open(file, 'r').readlines()[i].split('|')
    return listOfdata


def count(dic):  # count lines
    file = open(dic, "r")
    count_line = 0
    for line in file:
        count_line += 1
    file.close
    return count_line


def find(data, index,  file):
    for i in range(count(file)):
        y = open(file, "r").readlines()[i].split('|')
        if y[index] == data:
            return [i, y]


def listOfdats(data, index,  file):
    listOfData = []
    for i in range(count(file)):
        y = open(file, "r").readlines()[i].split('|')
        if y[index] == data:
            listOfData.append([i, y])
    return listOfData


def Change_Data(ID, dic, new_data):
    file = open(dic, 'r')
    data = file.readlines()
    i = find(ID, 0, dic)
    data[i[0]] = stri(new_data)
    with open(dic, 'w') as file:
        file.writelines(data)
    return data


def Clear_Data(ID, dic):
    file = open(dic, 'r')
    data = file.readlines()
    i = find(ID, 0, dic)
    data.pop(i[0])
    with open(dic, 'w') as file:
        file.writelines(data)


def Check_in(dic):
    file = open(dic, 'r')
    data = file.readlines()
    for i in range(len(data)):
        if len(data[i]) == 1 and data[i] == '\n':
            data.pop(i)
    if data[-1].find('\n') != -1:
        data[-1] = data[-1][:-2]
    with open(dic, 'w') as file:
        file.writelines(data)
