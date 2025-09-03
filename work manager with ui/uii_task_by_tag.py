import ui_task_by_tag
import uii_secondpage
import round2
from importqt import *
class tsbt(QMainWindow, ui_task_by_tag.tsbt):
    def __init__(self,id):
        super().__init__()
        self.setWindowTitle('aaa')
        self.setupUi(self)
        self.show()
        data = round2.todo.task_by_tag()
        for i in range(len(data)):
            QtWidgets.QTreeWidgetItem(self.treeWidget)
        for i in range(len(data)):
            self.treeWidget.topLevelItem(i).setText(0, data[i][0])
            for j in range(1,len(data[i][1])):
                self.treeWidget.topLevelItem(i).setText(j, data[i][1][j-1])
        self.back.clicked.connect(lambda: self.backk(id))
        self.exit.clicked.connect(lambda: self.exitt())
    def backk(self,id):
        self.close()
        self.second = uii_secondpage.secondpage(id)
    def exitt(self):
        quit()