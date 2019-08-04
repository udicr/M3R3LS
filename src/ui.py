from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from widgets import *
import sys


class PicButton(QAbstractButton):
    def __init__(self, pixmap, parent=None):
        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()


class Overlay(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setPalette(QtGui.QPalette(QtCore.Qt.transparent))
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setBrush(QtGui.QColor(0, 0, 0, 120))
        qp.drawRect(-1, -1, self.width(), self.height())
        qp.end()


class MainWindow(QMainWindow):
    resized = QtCore.pyqtSignal()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(0, 0, 960, 640)
        self.setWindowTitle("M3R3LS - Nine Man Morris aka. MÜHLE ")
        self.initUI()
        self.resized.connect(self.resizedwin)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(MainWindow, self).resizeEvent(event)

    def initUI(self):
        """
        styles
        """
        self.setStyleSheet("background-image: url(img/background.jpg)")
        """
        background
        """
        self.img = QImage("img/background.jpg")
        self.simg = self.img.scaled(QSize(self.width(), self.height()))
        palette = QPalette()
        palette.setBrush(10, QBrush(self.simg))
        self.setPalette(palette)
        """
        layout and widgets
        """

        self.horizontalGroupBox = QGroupBox()
        self.setCentralWidget(self.horizontalGroupBox)

        self.gamewidget = Game_Widget()
        self.scorewidget = Score_Widget()

        b = min([self.height() - 60, self.width() - 360])
        self.gamewidget.resize(b, b)
        self.scorewidget.resize(self.width() - b - 90, b - 40)
        self.scorewidget.move(self.width() - 30 - (self.width() - b - 90), 50)

        self.horizontalGroupBox.move(30,30)
        self.horizontalGroupBox.resize(self.width()-100,self.height()-100)
        _layout = QGridLayout(self.horizontalGroupBox)
        _layout.addWidget(self.gamewidget,0,0)
        _layout.addWidget(self.scorewidget,0,1)
        _layout.setHorizontalSpacing(50)
        _layout.setColumnMinimumWidth(0,self.height())


        self.horizontalGroupBox.setLayout(_layout)
        self.gamewidget.hide()
        self.scorewidget.hide()
        self.resize(self.width(),self.height())






        #self.gamewidget.hide()
        #self.scorewidget.hide()

        """
        self.gamewidget = Game_Widget()
        self.gamewidget.resize(self.height() - 60, self.height() - 60)
        self.gamewidget.move(30,30)
        self.gamewidget.hide()
        """

        """
        self.boardlabel = QLabel(self)   #todo make a container
        self.img2 = QImage("img/board.jpg")
        self.simg2 = self.img2.scaled(QSize(self.height() - 60, self.height() - 60))
        self.boardlabel.setPixmap(QPixmap.fromImage(self.simg2))
        self.boardlabel.resize(self.height() - 60, self.height() - 60)
        self.boardlabel.move(30, 30)
        self.boardlabel.hide()
        """

        """
        self.scorewidget = Score_Widget()
        self.scorewidget.resize(self.width() - self.height() + 60 - 90, self.height() - 100)
        self.scorewidget.move(self.width() -30 - (self.width() - self.height() + 60 - 90) , 50)
        self.scorewidget.hide()
        """

        """
        self.scoreboardlabel = QLabel(self)  #todo make a container
        self.img3 = QImage("img/scoreboard.png")
        self.simg3 = self.img3.scaled(QSize(self.width() - self.height() + 60 - 90, self.height() - 100))
        self.scoreboardlabel.setPixmap(QPixmap.fromImage(self.simg3))
        self.scoreboardlabel.resize(self.width() - self.height() + 60 - 90, self.height() - 100)
        self.scoreboardlabel.move(self.width() -30 - (self.width() - self.height() + 60 - 90) , 50)
        self.scoreboardlabel.hide()
        """

        """
        overlay
        """
        self.overlay = Overlay(self)
        self.overlay.resize(self.width() + 1, self.height() + 1)

        """
        menu
        """
        self.menushown = True
        self.menu = PicButton(QPixmap("img/menu.png"), self)
        self.menu.resize(32, 32)
        self.menu.clicked.connect(self.menu_pressed)
        self.menu.move(self.width() - 40, 8)

        self.b_newgame = PicButton(QPixmap("img/button_new-game.png"), self)
        self.b_newgame.resize(160, 40)
        self.b_newgame.clicked.connect(self.newgame)
        self.b_newgame.move(self.width() / 2 - 80, self.height() / 2 - 50)

        self.b_quitgame = PicButton(QPixmap("img/button_quit-game.png"), self)
        self.b_quitgame.resize(160, 40)
        self.b_quitgame.clicked.connect(self.quitgame)
        self.b_quitgame.move(self.width() / 2 - 80, self.height() / 2 + 10)

        self.whichgame = False
        self.game_started = False
        g = abs(min([100, self.width() / 2 - 60]))

        self.b_player = PicButton(QPixmap("img/hoodie.png"), self)
        self.b_player.resize(g, g)
        self.b_player.clicked.connect(self.start_playergame)
        self.b_player.move(self.width() / 2 - g - 20, self.height() / 2)
        self.b_player.hide()

        self.b_com = PicButton(QPixmap("img/processor.png"), self)
        self.b_com.resize(g, g)
        self.b_com.clicked.connect(self.start_comgame)
        self.b_com.move(self.width() / 2 + 20, self.height() / 2)
        self.b_com.hide()


    def showgame(self):
        self.overlay.hide()
        #self.boardlabel.show()
        #self.scoreboardlabel.show()
        self.gamewidget.show()
        self.scorewidget.show()

    def hidegame(self):
        #self.boardlabel.hide()
        self.gamewidget.hide()
        #self.scoreboardlabel.hide()
        self.scorewidget.hide()

    def start_playergame(self):
        self.hide_whichgame()
        self.game_started = True
        self.showgame()
        print("Starting Game against Player")

    def start_comgame(self):
        self.hide_whichgame()
        self.game_started = True
        self.showgame()
        print("Starting Game against COM")

    def newgame(self):
        self.hidegame()
        if self.game_started:
            self.game_started = False
        print("new")
        self.hide_menu()
        self.whichgame = True
        self.b_com.show()
        self.b_player.show()
        g = abs(min([100, self.width() / 2 - 60]))
        self.b_player.resize(g, g)
        self.b_player.move(self.width() / 2 - g - 20, self.height() / 2)
        self.b_com.resize(g, g)
        self.b_com.move(self.width() / 2 + 20, self.height() / 2)

    def quitgame(self):
        self.close()

    def show_menu(self):
        self.overlay.show()
        if self.whichgame:
            self.hide_whichgame()
        self.b_newgame.move(self.width() / 2 - 80, self.height() / 2 - 50)
        self.b_quitgame.move(self.width() / 2 - 80, self.height() / 2 + 10)
        self.menushown = True
        self.b_newgame.show()
        self.b_quitgame.show()
        print("appear")

    def hide_menu(self):
        if self.game_started:
            self.overlay.hide()
        self.b_quitgame.hide()
        self.b_newgame.hide()
        self.menushown = False
        print("disappear")

    def hide_whichgame(self):
        self.whichgame = False
        self.b_player.hide()
        self.b_com.hide()

    def resizedwin(self):
        self.simg = self.img.scaled(QSize(self.width(), self.height()))
        palette = QPalette()
        palette.setBrush(10, QBrush(self.simg))
        self.setPalette(palette)
        self.overlay.resize(self.width() + 1, self.height() + 1)
        self.menu.move(self.width() - 40, 8)
        if self.menushown:
            self.b_newgame.move(self.width() / 2 - 80, self.height() / 2 - 50)
            self.b_quitgame.move(self.width() / 2 - 80, self.height() / 2 + 10)
        if self.whichgame:
            g = abs(min([100, self.width() / 2 - 60]))
            self.b_player.resize(g, g)
            self.b_player.move(self.width() / 2 - g - 20, self.height() / 2)
            self.b_com.resize(g, g)
            self.b_com.move(self.width() / 2 + 20, self.height() / 2)
        if self.game_started:
            """
            b = min([self.height() - 60, self.width() - 360])
            self.simg2 = self.img2.scaled(QSize(b, b))
            self.boardlabel.setPixmap(QPixmap.fromImage(self.simg2))
            self.boardlabel.resize(b, b)
            """
            b = min([self.height() - 60, self.width() - 360])
            self.gamewidget.resize(b,b)
            self.scorewidget.resize(self.width() - b - 90, b - 40)
            self.scorewidget.move(self.width() - 30 - (self.width() - b - 90), 50)
            """
            self.simg3 = self.img3.scaled(QSize(self.width()- b - 90, b -40 ))
            self.scoreboardlabel.setPixmap(QPixmap.fromImage(self.simg3))
            self.scoreboardlabel.resize(self.width() - b - 90, b - 40)
            self.scoreboardlabel.move(self.width() - 30 - (self.width() - b - 90), 50)
            """

    def menu_pressed(self):
        if self.menushown and self.game_started:
            self.hide_menu()
            self.menushown = False
        else:
            self.show_menu()
            self.menushown = True


def window():
    app = QApplication(sys.argv)
    win = MainWindow()

    win.show()
    sys.exit(app.exec_())


window()