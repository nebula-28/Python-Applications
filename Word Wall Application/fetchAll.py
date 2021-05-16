from PyQt5 import QtCore, QtGui, QtWidgets
from definition import Definition
from synonyms import Synonyms
from antonym import Antonyms
from sentences import Sentences
from phonetics import Phonetics
from dbConnect import DbConnect
import re


class Fetch_All(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.head_label = QtWidgets.QLabel(self.centralwidget)
        self.head_label.setGeometry(QtCore.QRect(10, 10, 191, 16))
        self.head_label.setAutoFillBackground(True)
        self.head_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.head_label.setObjectName("head_label")
        self.word_label = QtWidgets.QLabel(self.centralwidget)
        self.word_label.setGeometry(QtCore.QRect(40, 60, 41, 16))
        self.word_label.setObjectName("word_label")
        self.word_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.word_line_edit.setGeometry(QtCore.QRect(90, 60, 181, 20))
        self.word_line_edit.setObjectName("word_line_edit")
        self.defn_label = QtWidgets.QLabel(self.centralwidget)
        self.defn_label.setGeometry(QtCore.QRect(10, 120, 61, 16))
        self.defn_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.defn_label.setObjectName("defn_label")
        self.defn_text_label = QtWidgets.QLabel(self.centralwidget)
        self.defn_text_label.setGeometry(QtCore.QRect(90, 120, 691, 101))
        self.defn_text_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.defn_text_label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.defn_text_label.setWordWrap(True)
        self.defn_text_label.setObjectName("defn_text_label")
        self.syn_label = QtWidgets.QLabel(self.centralwidget)
        self.syn_label.setGeometry(QtCore.QRect(10, 350, 61, 16))
        self.syn_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.syn_label.setObjectName("syn_label")
        self.syn_text_label = QtWidgets.QLabel(self.centralwidget)
        self.syn_text_label.setGeometry(QtCore.QRect(90, 350, 691, 61))
        self.syn_text_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.syn_text_label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.syn_text_label.setWordWrap(True)
        self.syn_text_label.setObjectName("syn_text_label")
        self.antonym_text_label = QtWidgets.QLabel(self.centralwidget)
        self.antonym_text_label.setGeometry(QtCore.QRect(90, 430, 691, 31))
        self.antonym_text_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.antonym_text_label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.antonym_text_label.setWordWrap(True)
        self.antonym_text_label.setObjectName("antonym_text_label")
        self.ant_label = QtWidgets.QLabel(self.centralwidget)
        self.ant_label.setGeometry(QtCore.QRect(10, 430, 61, 16))
        self.ant_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.ant_label.setObjectName("ant_label")
        self.phn_text_label = QtWidgets.QLabel(self.centralwidget)
        self.phn_text_label.setGeometry(QtCore.QRect(90, 480, 691, 21))
        self.phn_text_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.phn_text_label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.phn_text_label.setWordWrap(True)
        self.phn_text_label.setObjectName("phn_text_label")
        self.phn_label = QtWidgets.QLabel(self.centralwidget)
        self.phn_label.setGeometry(QtCore.QRect(10, 480, 61, 16))
        self.phn_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.phn_label.setObjectName("phn_label")
        self.sent_label = QtWidgets.QLabel(self.centralwidget)
        self.sent_label.setGeometry(QtCore.QRect(10, 230, 61, 16))
        self.sent_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.sent_label.setObjectName("sent_label")
        self.sent_text_label = QtWidgets.QLabel(self.centralwidget)
        self.sent_text_label.setGeometry(QtCore.QRect(90, 230, 691, 111))
        self.sent_text_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sent_text_label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.sent_text_label.setWordWrap(True)
        self.sent_text_label.setObjectName("sent_text_label")
        self.search_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.search_bttn.setGeometry(QtCore.QRect(290, 60, 75, 23))
        self.search_bttn.setObjectName("search_bttn")
        self.save_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.save_bttn.setGeometry(QtCore.QRect(400, 510, 101, 23))
        self.save_bttn.setObjectName("save_bttn")
        self.close_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.close_bttn.setGeometry(QtCore.QRect(320, 510, 75, 23))
        self.close_bttn.setObjectName("close_bttn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.search_bttn.clicked.connect(self.fetch_all_info)
        self.close_bttn.clicked.connect(MainWindow.close)
        self.save_bttn.clicked.connect(self.save_words)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.head_label.setText(_translate("MainWindow", "Fetch all information about the word "))
        self.word_label.setText(_translate("MainWindow", "Word"))
        self.word_line_edit.setPlaceholderText(_translate("MainWindow", "Please enter your word here"))
        self.defn_label.setText(_translate("MainWindow", "Definition"))
        self.defn_text_label.setText(_translate("MainWindow", "Definition"))
        self.syn_label.setText(_translate("MainWindow", "Synonyms"))
        self.syn_text_label.setText(_translate("MainWindow", "Synonym"))
        self.antonym_text_label.setText(_translate("MainWindow", "Antonym"))
        self.ant_label.setText(_translate("MainWindow", "Antonyms"))
        self.phn_text_label.setText(_translate("MainWindow", "Phonetics"))
        self.phn_label.setText(_translate("MainWindow", "Phonetics"))
        self.sent_label.setText(_translate("MainWindow", "Sentences"))
        self.sent_text_label.setText(_translate("MainWindow", "Sentences"))
        self.search_bttn.setText(_translate("MainWindow", "Search"))
        self.save_bttn.setText(_translate("MainWindow", "Save this word"))
        self.close_bttn.setText(_translate("MainWindow", "Close"))

    def fetch_all_info(self):
        try:
            user_word=self.word_line_edit.text()
            definition=Definition.search_word(self)
            synonym=Synonyms.search_synonym(self)
            antonym=Antonyms.search_antonym(self)
            sentence=Sentences.get_sentences(self)
            phonetic=Phonetics.search_phonetics(self)
            
        except Exception as e:
            print('Something went wrong , Please try again !! ')
        
        return user_word,definition,synonym,antonym ,phonetic,sentence

    def save_words(self):
        
        word_data=self.fetch_all_info()
        user_word=str(word_data[0]).replace("'","")
        definition=str(word_data[1]).replace("'","")
        synonym=str(word_data[2]).replace("'","")
        antonym=str(word_data[3]).replace("'","")
        phonetics=str(word_data[4]).replace("'","")
        sentences=str(word_data[5]).replace("'","")

        db=DbConnect()
        db.insert_word(user_word,definition,synonym,antonym ,phonetics,sentences)
        print("This word is inserted")
        #db.fetch_all()
       


