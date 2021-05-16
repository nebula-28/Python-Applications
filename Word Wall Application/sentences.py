from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup

class Sentences(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.search_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.search_bttn.setGeometry(QtCore.QRect(510, 30, 75, 23))
        self.search_bttn.setObjectName("search_bttn")
        self.search_bttn.clicked.connect(self.get_sentences)
        self.word_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.word_line_edit.setGeometry(QtCore.QRect(290, 30, 211, 20))
        self.word_line_edit.setObjectName("word_line_edit")
        self.ex_title_label = QtWidgets.QLabel(self.centralwidget)
        self.ex_title_label.setGeometry(QtCore.QRect(220, 30, 61, 16))
        self.ex_title_label.setObjectName("ex_title_label")
        self.close_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.close_bttn.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.close_bttn.setObjectName("close_bttn")
        self.close_bttn.clicked.connect(MainWindow.close)
        self.sent_text_label = QtWidgets.QLabel(self.centralwidget)
        self.sent_text_label.setGeometry(QtCore.QRect(10, 60, 771, 481))
        self.sent_text_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.sent_text_label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.sent_text_label.setWordWrap(True)
        self.sent_text_label.setObjectName("sent_text_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_bttn.setText(_translate("MainWindow", "Search"))
        #self.word_line_edit.setText(_translate("MainWindow", "Please enter your word here"))
        self.ex_title_label.setText(_translate("MainWindow", "Examples"))
        self.close_bttn.setText(_translate("MainWindow", "Close"))
        self.sent_text_label.setText(_translate("MainWindow", "Sentences will be printed here "))
        self.word_line_edit.setPlaceholderText("Please enter your word here ")


    def get_sentences(self):
        try:
            word=self.word_line_edit.text()
            url='https://sentence.yourdictionary.com/'+str(word)
            webpage_request=requests.get(url)
            soup_object=BeautifulSoup(webpage_request.content,'html5lib')
            sentences_text=""
            list_of_sntncs=[]
            for sent in soup_object.find_all('span',attrs={'class':'sentence-item__text'}):
                list_of_sntncs.append(sent.text)
            for i in range(len(list_of_sntncs)):
                if i==10:
                    break
                else:
                    sentences_text = sentences_text + str(i+1) + ". " + list_of_sntncs[i] + "\n"
            self.sent_text_label.setText(sentences_text)
        except AttributeError as e:
            self.sent_text_label.setText("Oops !! Thesaurus is not able to find your word.....")
        except:
            self.sent_text_label.setText("Something went wrong")
        return str(sentences_text)
