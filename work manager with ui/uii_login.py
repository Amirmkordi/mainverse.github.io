import ui_login
import uii_secondpage
import uii_singup
import round2
from importqt import *


class login(QMainWindow, ui_login.login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login.clicked.connect(lambda: self.loginn())
        self.send_code.clicked.connect(lambda: self.code_check())
        self.singup.clicked.connect(lambda: self.singupp())
        self.show()
    def singupp(self):
        self.close()
        self.aa = uii_singup.singup()
    def code_check(self):
        a = round2.todo
        c = a.login(self.user.text(), self.password.text())
        if c[0]:
            self.rand = c[0]
            self.status.setStyleSheet("color:green")
            self.status.setText(c[1])
        if c[0] == False:
            self.status.setStyleSheet("color:red")
            self.status.setText(c[1])
    def loginn(self):
        a = round2.todo
        b = a.check_sms(self.code.value(),self.rand)
        if b[0]:
            self.status.setStyleSheet("color:green")
            self.status.setText(f'hello {b[1]}')
            self.close()
            self.aa = uii_secondpage.secondpage(b[1])
        if b[0] == False:
            self.status.setStyleSheet("color:red")
            self.status.setText(b[1])
