import PyDictionary
from PyDictionary import PyDictionary
from PyQt5 import QtCore, QtGui, QtWidgets


class Definition(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1040, 570)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.defn_title_label = QtWidgets.QLabel(self.centralwidget)
        self.defn_title_label.setGeometry(QtCore.QRect(20, 30, 351, 51))
        self.defn_title_label.setObjectName("defn_title_label")
        self.defn_text_label = QtWidgets.QLabel(self.centralwidget)
        self.defn_text_label.setGeometry(QtCore.QRect(20, 130, 801, 411))
        self.defn_text_label.setAutoFillBackground(True)
        self.defn_text_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.defn_text_label.setTextFormat(QtCore.Qt.PlainText)
        self.defn_text_label.setWordWrap(True)
        self.defn_text_label.setObjectName("defn_text_label")
        self.back_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.back_bttn.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.back_bttn.setObjectName("back_bttn")
        self.back_bttn.clicked.connect(MainWindow.close)
        #self.back_bttn.clicked.connect(self.close)
        #self.back_bttn.clicked.connect(self.back_to_menu)
        self.word_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.word_line_edit.setGeometry(QtCore.QRect(20, 90, 261, 20))
        self.word_line_edit.setObjectName("word_line_edit")
        self.search_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.search_bttn.setGeometry(QtCore.QRect(310, 90, 75, 23))
        self.search_bttn.setObjectName("search_bttn")
        self.search_bttn.clicked.connect(self.search_word)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.defn_text_label.setScaledContents(False)	
        self.defn_text_label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.defn_title_label.setText(_translate("MainWindow", "Definitions:"))
        self.defn_text_label.setText(_translate("MainWindow", "List of Definitions will be printed here "))
        self.back_bttn.setText(_translate("MainWindow", "Back"))
        #self.word_line_edit.setText(_translate("MainWindow", "Please enter your word here "))
        self.word_line_edit.setPlaceholderText("Please enter your word here ")  #This is placeholder text which is highlighted and on top you can write your input.This is the basic difference between setText and setPlaceholderText
        self.search_bttn.setText(_translate("MainWindow", "search"))

    #def search_word(self):
    #    word=self.word_line_edit.text()
    #    dictionary=PyDictionary()
    #    meaning=dictionary.meaning(word)
    #    self.defn_text_label.setText(str(meaning))

    def search_word(self):
        word=self.word_line_edit.text()
        if len(word) != 0:
            dictionary=PyDictionary()
            dict_obj=dictionary.meaning(word) #This return a dictionary where keys= "parts of Speech" and items='respective meanings"
            meanings=''
            for i in dict_obj.keys():
                meanings=meanings+"".join('Part of Speech : '+ i +' | Definitions : '+str(dict_obj.get(i)))+'\n'
            self.defn_text_label.setText(meanings)
        else:
            self.defn_text_label.setText("Something went wrong ! No meaning found !")
        return str(meanings)



