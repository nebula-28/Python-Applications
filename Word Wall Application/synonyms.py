from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup


class Synonyms(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.close_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.close_bttn.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.close_bttn.setObjectName("close_bttn")
        self.close_bttn.clicked.connect(MainWindow.close)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label.setObjectName("label")
        self.word_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.word_line_edit.setGeometry(QtCore.QRect(10, 90, 211, 20))
        self.word_line_edit.setObjectName("lineEdit")
        self.srch_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.srch_bttn.setGeometry(QtCore.QRect(240, 90, 75, 23))
        self.srch_bttn.setObjectName("srch_bttn")
        self.srch_bttn.clicked.connect(self.search_synonym)
        self.syn_text_label = QtWidgets.QLabel(self.centralwidget)
        self.syn_text_label.setGeometry(QtCore.QRect(10, 129, 771, 381))
        self.syn_text_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.syn_text_label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.syn_text_label.setObjectName("syn_text_label")
        self.syn_text_label.setWordWrap(True)
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
        self.label.setText(_translate("MainWindow", "Synonyms:"))
        #self.word_line_edit.setText(_translate("MainWindow", "Please enter your word here"))
        self.word_line_edit.setPlaceholderText("Please enter your word here ")  #This is placeholder text which is highlighted and on top you can write your input.This is the basic difference between setText and setPlaceholderText
        self.srch_bttn.setText(_translate("MainWindow", "Search"))
        self.syn_text_label.setText(_translate("MainWindow", " List of Synonyms will be printed here "))

    def search_synonym(self):
        try:
            word=self.word_line_edit.text()
            url='https://www.thesaurus.com/browse/'+str(word)
            webpage_request=requests.get(url)
            soup_object=BeautifulSoup(webpage_request.content,'html5lib')
            head_list = soup_object.find('div',attrs={'class':'css-i3pbo e1i572590'}).find('ul')
            list_of_synonyms=[]
            for li in head_list.find_all("li"):
                list_of_synonyms.append(li.text)
            self.syn_text_label.setText(str(list_of_synonyms))
        except AttributeError as e:
            self.syn_text_label.setText("Oops !! Thesaurus is not able to find your word.....")
        except:
            print("Something went wrong")
        return str(list_of_synonyms)

