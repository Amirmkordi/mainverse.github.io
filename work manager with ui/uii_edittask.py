import ui_main
import ui_edittask
import uii_secondpage
import round2
from importqt import *
class edit(QMainWindow, ui_edittask.edit):
    def __init__(self,id):
        super().__init__()
        self.setWindowTitle('aaa')
        self.setupUi(self)
        self.show()
        self.IDs.setMinimum(1)
        self.IDs.setMaximum(round2.todo.id)
        self.back.clicked.connect(lambda: self.backk(id))
        self.exit.clicked.connect(lambda: self.exitt())
        self.add_tag.clicked.connect(lambda: self.add_option())
        self.IDs.valueChanged.connect(lambda: self.access(id))
        self.edit.clicked.connect(lambda: self.add(id))
    def access(self,idp):
        b = round2.todoo().editable(self.IDs.value(), idp)
        if b[0] == True:self.show_option(idp)
        else:
            self.Status.setText(b[1])
            self.Titlel.setText('')
            self.detaill.setText('')
            try:
                for i in range(len(self.horizontalLayout)):
                    self.labell[i].deleteLater()
                    self.lineEdit[i].deleteLater()
                    self.horizontalLayout[i].deleteLater()
            except:pass
            self.Status.setStyleSheet("color:red")
    def show_option(self,idp):
        b = round2.todo.editable(self.IDs.value(),idp)[1]
        self.Status.setText('')
        self.Titlel.setText(b[0])
        self.detaill.setText(b[1])
        time = b[2].split('-')
        self.deadlinel.setDateTime(QtCore.QDateTime(QtCore.QDate(int(time[0]),int(time[1]),int(time[2])), QtCore.QTime(int(time[3]),int(time[4]),00)))
        tag = b[3].split(',')
        a= len(tag)
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
            self.lineEdit[i].setText(tag[i])
            self.horizontalLayout[i].addWidget(self.lineEdit[i])
        if b[4] == 'False':
            self.done.setChecked(False)
        elif b[4] == 'True':
            self.done.setChecked(True)
    def add_option(self):
        self.labell.append(None)
        self.lineEdit.append(None)
        self.horizontalLayout.append(None)
        i = len(self.horizontalLayout)-1
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
    def add(self,idp):
        b = round2.todoo().editable(self.IDs.value(), idp)
        if b[0] == True:
            deadline = f'{self.deadlinel.date().year()}-{self.deadlinel.date().month()}-{self.deadlinel.date().day()}-{self.deadlinel.time().hour()}-{self.deadlinel.time().minute()}'
            tag = list()
            for i in range(len(self.lineEdit)):tag.append(self.lineEdit[i].text())
            if self.done.checkState() == 2:status = 'True'
            else :status = 'False'
            b = round2.todo.edit(self.IDs.value(), self.Titlel.text(), self.detaill.text(), deadline, ','.join(tag), status,idp)
            if b[0] == True:self.Status.setStyleSheet("color:green")
            else:self.Status.setStyleSheet("color:red")
            self.Status.setText(b[1])
        else:
            self.Status.setText(b[1])
            self.Titlel.setText('')
            self.detaill.setText('')
            try:
                for i in range(len(self.horizontalLayout)):
                    self.labell[i].deleteLater()
                    self.lineEdit[i].deleteLater()
                    self.horizontalLayout[i].deleteLater()
            except:pass
            self.Status.setStyleSheet("color:red")
    def backk(self,id):
        self.close()
        self.second = uii_secondpage.secondpage(id)
    def exitt(self):
        quit()
if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("amlak kahfi")
    wnd = edit('P_316')
    app.exec()