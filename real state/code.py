from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import mainwindow
if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("kor")
    wnd = mainwindow.mainwindow()
    app.exec()