import ui_group
import uii_secondpage
import round2
from importqt import *
class group(QMainWindow, ui_group.group):
    def __init__(self,id):
        super().__init__()
        self.setWindowTitle('aaa')
        self.setupUi(self)
        self.show()
        data = round2.todo.group()
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
if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("amlak kahfi")
    # wnd = login()
    wnd = group('P_168')
    app.exec()