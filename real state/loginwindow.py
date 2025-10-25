from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from ui import ui_loginwindow
class loginwindow(QMainWindow, ui_loginwindow.Ui_loginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.save())
        self.show()
    def save(self):
        self.close()