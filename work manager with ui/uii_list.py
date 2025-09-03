import uii_secondpage
import ui_list
import round2
from importqt import *
class list(QMainWindow, ui_list.list):
    def __init__(self,id):
        super().__init__()
        self.setWindowTitle('aaa')
        self.setupUi(self)
        self.show()
        data = round2.todo.task_list()
        for i in range(len(data)):
            QtWidgets.QTreeWidgetItem(self.treeWidget)
        for i in range(len(data)):
            for j in range(len(data[i])):
                self.treeWidget.topLevelItem(i).setText(j, data[i][j])
        self.back.clicked.connect(lambda: self.backk(id))
        self.exit.clicked.connect(lambda: self.exitt())
    def backk(self,id):
        self.close()
        self.second = uii_secondpage.secondpage(id)
    def exitt(self):
        quit()