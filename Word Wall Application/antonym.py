import PyDictionary
from PyDictionary import PyDictionary
from PyQt5 import QtCore, QtGui, QtWidgets


class Antonyms(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.close_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.close_bttn.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.close_bttn.setObjectName("close_bttn")
        self.close_bttn.clicked.connect(MainWindow.close)
        self.search_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.search_bttn.setGeometry(QtCore.QRect(240, 90, 75, 23))
        self.search_bttn.setObjectName("search_bttn")
        self.search_bttn.clicked.connect(self.search_antonym)
        self.word_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.word_line_edit.setGeometry(QtCore.QRect(10, 90, 211, 20))
        self.word_line_edit.setObjectName("word_line_edit")
        self.antonym_text_label = QtWidgets.QLabel(self.centralwidget)
        self.antonym_text_label.setGeometry(QtCore.QRect(10, 129, 771, 381))
        self.antonym_text_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.antonym_text_label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.antonym_text_label.setWordWrap(True)
        self.antonym_text_label.setObjectName("antonym_lebel")
        self.antonym_title_label = QtWidgets.QLabel(self.centralwidget)
        self.antonym_title_label.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.antonym_title_label.setObjectName("antonym_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.close_bttn.setText(_translate("MainWindow", "Close"))
        self.search_bttn.setText(_translate("MainWindow", "Search"))
        #self.word_line_edit.setText(_translate("MainWindow", "Please enter your word here"))
        self.antonym_text_label.setText(_translate("MainWindow", "List of Antonyms will be printed here "))
        self.antonym_title_label.setText(_translate("MainWindow", "Antonyms"))
        self.word_line_edit.setPlaceholderText("Please enter your word here ")  #This is placeholder text which is highlighted and on top you can write your input.This is the basic difference between setText and setPlaceholderText

    def search_antonym(self):
        try:
            word=self.word_line_edit.text()
            if len(word) != 0:
                dictionary=PyDictionary()
                antonym_list=dictionary.antonym(word) #This return a dictionary where keys= "parts of Speech" and items='respective meanings"
                synonyms=''
                self.antonym_text_label.setText(str(antonym_list))
            else:
                self.antonym_text_label.setText("No Text Entered")
        except Exception as e:
            self.antonym_text_label.setText("No Antonym Found")
        return str(antonym_list)
