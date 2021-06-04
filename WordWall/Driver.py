from main_menu import Menu
from definition import Definition
import sys
import PyDictionary
from PyDictionary import PyDictionary
from PyQt5 import QtCore, QtGui, QtWidgets


class Driver:
    def get_menu(self,menu_window):
        self.menu_ob = Menu()
        self.menu_ob.setupUi(menu_window)
        menu_window.show()
    
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    menu_window = QtWidgets.QMainWindow()
    drvr_ob=Driver()
    drvr_ob.get_menu(menu_window)
    #drvr_ob.get_word_defn(defn_window,menu_window)
    sys.exit(app.exec_())
