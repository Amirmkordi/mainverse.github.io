from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from ui import ui_mainwindow
import signupwindow
import loginwindow
class mainwindow(QMainWindow, ui_mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sin.clicked.connect(lambda: self.sinu())
        self.log.clicked.connect(lambda: self.logu())
        self.show()
    def sinu(self):
        signupapp = signupwindow.signupwindow()
        self.close()
    def logu(self):
        loginapp = loginwindow.loginwindow()
        self.close()