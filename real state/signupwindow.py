from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from ui import ui_signupwindow
class signupwindow(QMainWindow, ui_signupwindow.Ui_signupWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.save())
        self.show()
    def save(self):
        self.close()