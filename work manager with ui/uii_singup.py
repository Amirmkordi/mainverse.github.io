import ui_singup
import uii_login
import round2
from importqt import *


class singup(QMainWindow, ui_singup.singup):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exit.clicked.connect(lambda: self.exitt())
        self.SingUp.clicked.connect(lambda: self.singupp())
        self.back.clicked.connect(lambda: self.backk())
        self.show()
    def singupp(self):
        a =round2.todo.creat_user(self.username.text(),self.phonenumber.text(),self.pass1.text(),self.pass2.text())
        if a[0] == False:
            self.status.setStyleSheet("color:red")
            self.status.setText(f'<html><head/><body><p align=\"center\">{a[1]}</p></body></html>')
        else:
            self.status.setStyleSheet("color:green")
            self.status.setText(f'<html><head/><body><p align=\"center\">{a[1]}</p></body></html>')
    def backk(self):
        self.close()
        self.second = uii_login.login()
    def exitt(self):
        quit()