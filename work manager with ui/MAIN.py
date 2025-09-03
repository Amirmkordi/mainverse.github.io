from uii_login import *
from importqt import *
if __name__ == '__main__':
    app = QApplication([])
    wnd = login()
    app.exec()