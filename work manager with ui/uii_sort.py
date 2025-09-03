import uii_secondpage
import ui_sort
import round2
from importqt import *
class sort(QMainWindow, ui_sort.sort):
    def __init__(self,id):
        super().__init__()
        self.setWindowTitle('aaa')
        self.setupUi(self)
        self.show()
        if self.reverse.checkState() == 2:self.az = True
        else :self.az = False
        self.word = 'e'
        self.deadline.setChecked(True)
        self.deadline.toggled.connect(lambda: self.e())
        self.last_edited.toggled.connect(lambda: self.u())
        self.date_created.toggled.connect(lambda: self.c())
        self.reverse.stateChanged.connect(lambda: self.abz())
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.back.clicked.connect(lambda: self.backk(id))
        self.exit.clicked.connect(lambda: self.exitt())
    def showTime(self):
        data = round2.todo.sort(self.word, self.az)
        for i in range(self.treeWidget.topLevelItemCount()):
            self.treeWidget.takeTopLevelItem(0)
        for i in range(len(data)):
            QtWidgets.QTreeWidgetItem(self.treeWidget)
        for i in range(len(data)):
            for j in range(len(data[i])):
                self.treeWidget.topLevelItem(i).setText(j, data[i][j])
    def abz(self):
        if self.reverse.checkState() == 2:self.az = True
        else :self.az = False
    def e(self):
        self.word = 'e'
    def u(self):
        self.word = 'u'
    def c(self):
        self.word = 'c'
    def backk(self,id):
        self.close()
        self.second = uii_secondpage.secondpage(id)
    def exitt(self):
        quit()