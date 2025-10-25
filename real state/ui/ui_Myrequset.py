from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Myads(object):
    def setupUi(self, Myads):
        Myads.setObjectName("Myads")
        Myads.resize(400, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(Myads)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 381, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)

        self.retranslateUi(Myads)
        QtCore.QMetaObject.connectSlotsByName(Myads)

    def retranslateUi(self, Myads):
        _translate = QtCore.QCoreApplication.translate
        Myads.setWindowTitle(_translate("Myads", "Dialog"))
        self.label_2.setText(_translate("Myads", "TextLabel"))
        self.label.setText(_translate("Myads", "TextLabel"))
        self.label_3.setText(_translate("Myads", "TextLabel"))
        self.label_4.setText(_translate("Myads", "TextLabel"))
        self.label_5.setText(_translate("Myads", "TextLabel"))
        self.label_6.setText(_translate("Myads", "TextLabel"))
