import ui
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    win = ui.MainWindow()

    win.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    window()