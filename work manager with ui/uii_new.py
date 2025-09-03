import ui_main
import ui_new
import uii_secondpage
import round2
from ui_new import *
from importqt import *
class new(QMainWindow, ui_new.new):
    def __init__(self,id):
        super().__init__()
        self.setWindowTitle('aaa')
        self.setupUi(self)
        self.show()
        self.back.clicked.connect(lambda: self.backk(id))
        self.exit.clicked.connect(lambda: self.exitt())
        self.toption.valueChanged.connect(lambda: self.add_option())
        self.add_new.clicked.connect(lambda: self.add(id))
    def add(self,id):
        option = []
        for i in range(self.toption.value()):
            option.append(self.lineEdit[i].text())
        deadline = f'{self.deadlinee.date().year()}-{self.deadlinee.date().month()}-{self.deadlinee.date().day()}-{self.deadlinee.time().hour()}-{self.deadlinee.time().minute()}'
        new = round2.todo.new_task(self.title.text(), self.detail.text(), deadline, ','.join(option), id)
        self.Status.setStyleSheet("color:green")
        self.Status.setText(f'<html><head/><body><p align=\"center\">{new[1]}</p></body></html>')
    def add_option(self):
        a=self.toption.value()
        try:
            for i in range(len(self.horizontalLayout)):
                self.labell[i].deleteLater()
                self.lineEdit[i].deleteLater()
                self.horizontalLayout[i].deleteLater()
        except:pass
        self.labell=[None]*a
        self.lineEdit=[None]*a
        self.horizontalLayout =[None]*a
        for i in range(a):
            self.horizontalLayout[i] = QtWidgets.QHBoxLayout()
            self.horizontalLayout[i].setObjectName("horizontalLayout_9")
            self.labell[i] = QtWidgets.QLabel(self.centralwidget)
            self.labell[i].setObjectName(f"label_{i+1}")
            self.horizontalLayout[i].addWidget(self.labell[i])
            self.labell[i].setText(f"tag {i+1} :")
            self.gridLayout.addLayout(self.horizontalLayout[i], i, 0, 1, 1)
            self.lineEdit[i] = QtWidgets.QLineEdit(self.centralwidget)
            self.lineEdit[i].setObjectName(f"lineEdit_{i+1}")
            self.horizontalLayout[i].addWidget(self.lineEdit[i])
            
            
    def backk(self,id):
        self.close()
        self.second = uii_secondpage.secondpage(id)
    def exitt(self):
        quit()