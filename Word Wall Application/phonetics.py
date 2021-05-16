from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup
import json

class Phonetics(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 179)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.search_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.search_bttn.setGeometry(QtCore.QRect(510, 30, 75, 23))
        self.search_bttn.setObjectName("search_bttn")
        self.search_bttn.clicked.connect(self.search_phonetics)
        self.phonetics_title_label = QtWidgets.QLabel(self.centralwidget)
        self.phonetics_title_label.setGeometry(QtCore.QRect(220, 30, 61, 16))
        self.phonetics_title_label.setObjectName("phonetics_title_label")
        self.word_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.word_line_edit.setGeometry(QtCore.QRect(290, 30, 211, 20))
        self.word_line_edit.setObjectName("word_line_edit")
        self.phn_text_label = QtWidgets.QLabel(self.centralwidget)
        self.phn_text_label.setGeometry(QtCore.QRect(170, 70, 451, 61))
        self.phn_text_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.phn_text_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.phn_text_label.setWordWrap(True)
        self.phn_text_label.setObjectName("phn_text_label")
        self.close_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.close_bttn.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.close_bttn.setObjectName("close_bttn")
        self.close_bttn.clicked.connect(MainWindow.close)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_bttn.setText(_translate("MainWindow", "Search"))
        self.phonetics_title_label.setText(_translate("MainWindow", "Phonetics"))
        #self.word_line_edit.setText(_translate("MainWindow", "Please enter your word here"))
        self.phn_text_label.setText(_translate("MainWindow", "Phonetics"))
        self.close_bttn.setText(_translate("MainWindow", "Close"))
        self.word_line_edit.setPlaceholderText("Please enter your word here ")

    def search_phonetics(self):
        try:
            word=self.word_line_edit.text()
            url='https://api.dictionaryapi.dev/api/v2/entries/en_US/'+str(word)
            webpage_request=requests.get(url)
            soup_object=BeautifulSoup(webpage_request.content,'html5lib')
            json_string=soup_object.text
            to_json_list=json.loads(json_string)
            phonetics=to_json_list[0]['phonetics'][0]['text']
            self.phn_text_label.setText(phonetics)
        except AttributeError as e:
            self.phn_text_label.setText("Oops !! Thesaurus is not able to find your word.....")
        except:
            self.phn_text_label.setText("Something went wrong")
        return str(phonetics)