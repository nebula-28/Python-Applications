from PyQt5 import QtCore, QtGui, QtWidgets


class SavedWords(object):
    def setupUi(self, Message):
        Message.setObjectName("Message")
        Message.resize(334, 131)
        self.centralwidget = QtWidgets.QWidget(Message)
        self.centralwidget.setObjectName("centralwidget")
        self.close_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.close_bttn.setGeometry(QtCore.QRect(130, 70, 75, 23))
        self.close_bttn.setObjectName("close_bttn")
        self.close_bttn.clicked.connect(Message.close)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 40, 71, 16))
        self.label.setObjectName("label")
        Message.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Message)
        self.statusbar.setObjectName("statusbar")
        Message.setStatusBar(self.statusbar)

        self.retranslateUi(Message)
        QtCore.QMetaObject.connectSlotsByName(Message)

    def retranslateUi(self, Message):
        _translate = QtCore.QCoreApplication.translate
        Message.setWindowTitle(_translate("Message", "Message"))
        self.close_bttn.setText(_translate("Message", "Close"))
        self.label.setText(_translate("Message", "Data is saved !!"))