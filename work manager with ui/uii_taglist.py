import uii_secondpage
import ui_taglist
import round2
from importqt import *
class taglist(QMainWindow, ui_taglist.taglist):
    def __init__(self,id):
        super().__init__()
        self.setWindowTitle('aaa')
        self.setupUi(self)
        self.show()
        self.taglist()
        self.back.clicked.connect(lambda: self.backk(id))
        self.exit.clicked.connect(lambda: self.exitt())
    def taglist(self):
        data = round2.todo.tag_list()
        x = len(data)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label = [None]*x
        if x%2 !=0:
            y=0
            for i in range(int(x/2)+1):
                self.label[y] = QtWidgets.QLabel(self.centralwidget)
                self.label[y].setObjectName(f"label {y}")
                self.gridLayout.addWidget(self.label[y], i, 1, 1, 1)
                self.label[y].setText(f'tag {y+1} : {data[y]}')
                self.label[y].setFont(font)
                y+=1
            for i in range(int(x/2)):
                self.label[y] = QtWidgets.QLabel(self.centralwidget)
                self.label[y].setObjectName(f"label {y}")
                self.gridLayout.addWidget(self.label[y], i, 2, 1, 1)
                self.label[y].setText(f'tag {y+1} : {data[y]}')
                self.label[y].setFont(font)
                y+=1
        else:
            y = 0
            for j in range(2):
                for i in range(int(x/2)):
                    self.label[y] = QtWidgets.QLabel(self.centralwidget)
                    self.label[y].setObjectName(f"label {y}")
                    self.gridLayout.addWidget(self.label[y], i, j, 1, 1)
                    self.label[y].setText(f'tag {y+1} : {data[y]}')
                    self.label[y].setFont(font)
                    y+=1
    def backk(self,id):
        self.close()
        self.second = uii_secondpage.secondpage(id)
    def exitt(self):
        quit()
if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("amlak kahfi")
    # wnd = login()
    wnd = taglist('P_168')
    app.exec()