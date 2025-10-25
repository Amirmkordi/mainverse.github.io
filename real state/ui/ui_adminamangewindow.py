from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_adminamangeWindow(object):
    def setupUi(self, adminamangeWindow):
        adminamangeWindow.setObjectName("adminamangeWindow")
        adminamangeWindow.resize(762, 200)
        self.centralwidget = QtWidgets.QWidget(adminamangeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 731, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        adminamangeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(adminamangeWindow)
        self.statusbar.setObjectName("statusbar")
        adminamangeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(adminamangeWindow)
        QtCore.QMetaObject.connectSlotsByName(adminamangeWindow)

    def retranslateUi(self, adminamangeWindow):
        _translate = QtCore.QCoreApplication.translate
        adminamangeWindow.setWindowTitle(_translate("adminamangeWindow", "adminamangeWindow"))
        self.pushButton_2.setText(_translate("adminamangeWindow", "accepet requset"))
        self.pushButton_3.setText(_translate("adminamangeWindow", "ad new admin"))
        self.pushButton.setText(_translate("adminamangeWindow", "all houses "))
