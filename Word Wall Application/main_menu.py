from PyQt5 import QtCore, QtGui, QtWidgets
from definition import Definition
from synonyms import Synonyms
from antonym import Antonyms
from sentences import Sentences
from phonetics import Phonetics
from fetchAll import Fetch_All

class Menu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(719, 574)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.defn_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.defn_bttn.setGeometry(QtCore.QRect(430, 150, 201, 41))
        self.defn_bttn.setObjectName("defn_bttn")
        self.ant_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.ant_bttn.setGeometry(QtCore.QRect(430, 250, 201, 41))
        self.ant_bttn.setObjectName("ant_bttn")
        self.phon_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.phon_bttn.setGeometry(QtCore.QRect(430, 300, 201, 41))
        self.phon_bttn.setObjectName("phon_bttn")
        self.ex_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.ex_bttn.setGeometry(QtCore.QRect(430, 350, 201, 41))
        self.ex_bttn.setObjectName("ex_bttn")
        self.syn_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.syn_bttn.setGeometry(QtCore.QRect(430, 200, 201, 41))
        self.syn_bttn.setObjectName("syn_bttn")
        self.fetch_all_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.fetch_all_bttn.setGeometry(QtCore.QRect(430, 400, 201, 41))
        self.fetch_all_bttn.setObjectName("fetch_all_bttn")
        self.flag_bttn = QtWidgets.QPushButton(self.centralwidget)
        self.flag_bttn.setGeometry(QtCore.QRect(430, 450, 201, 41))
        self.flag_bttn.setObjectName("flag_bttn")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(10, 100, 411, 441))
        self.title_label.setText("")
        self.title_label.setPixmap(QtGui.QPixmap("C:/Users/tiwar/Desktop/1.Project/VocabBuddy/images/main_menu_img.jpg"))
        self.title_label.setObjectName("title_label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 0, 351, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/tiwar/Desktop/1.Project/VocabBuddy/images/WORD_WALL.PNG"))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.defn_bttn.clicked.connect(self.get_definition)
        self.ant_bttn.clicked.connect(self.get_antonym)
        self.phon_bttn.clicked.connect(self.get_phonetics)
        self.ex_bttn.clicked.connect(self.get_sentences)
        self.syn_bttn.clicked.connect(self.get_synonyms)
        self.fetch_all_bttn.clicked.connect(self.get_fetcher)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Word Wall Application"))
        self.defn_bttn.setText(_translate("MainWindow", "Definitions"))
        self.ant_bttn.setText(_translate("MainWindow", "Antonym"))
        self.phon_bttn.setText(_translate("MainWindow", "Phonetics"))
        self.ex_bttn.setText(_translate("MainWindow", "Examples/Sentences"))
        self.syn_bttn.setText(_translate("MainWindow", "Synonyms"))
        self.fetch_all_bttn.setText(_translate("MainWindow", "Fetch all Info"))
        self.flag_bttn.setText(_translate("MainWindow", "Revise your Words"))

    def get_definition(self):
        self.defn_window= QtWidgets.QMainWindow()
        self.defn=Definition()
        self.defn.setupUi(self.defn_window)
        self.defn_window.show()

    def get_synonyms(self):
        self.syn_window= QtWidgets.QMainWindow()
        self.syn=Synonyms()
        self.syn.setupUi(self.syn_window)
        self.syn_window.show()

    def get_antonym(self):
        self.ant_window= QtWidgets.QMainWindow()
        self.ant=Antonyms()
        self.ant.setupUi(self.ant_window)
        self.ant_window.show()

    def get_sentences(self):
        self.sent_window= QtWidgets.QMainWindow()
        self.sent=Sentences()
        self.sent.setupUi(self.sent_window)
        self.sent_window.show()

    def get_phonetics(self):
        self.phn_window= QtWidgets.QMainWindow()
        self.phn=Phonetics()
        self.phn.setupUi(self.phn_window)
        self.phn_window.show()

    def get_fetcher(self):
        self.fetch_window= QtWidgets.QMainWindow()
        self.fetch=Fetch_All()
        self.fetch.setupUi(self.fetch_window)
        self.fetch_window.show()    