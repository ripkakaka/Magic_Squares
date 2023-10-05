from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

import sys

class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()

        self.setWindowTitle("Magic square")
        self.setGeometry(600, 500, 550, 400)

        self.btn_exit = QtWidgets.QPushButton(self)
        self.btn_exit.move(230, 225)
        self.btn_exit.setText("Выйти")
        self.btn_exit.setFixedWidth(115)
        self.btn_exit.clicked.connect(quit)

        self.App_text = QtWidgets.QLabel(self)
        self.App_text.setText("Магическй квадрат")
        self.App_text.move(165, 50)
        self.App_text.setFixedWidth(300)
        self.App_text.setFont(QtGui.QFont("Time", 18, QtGui.QFont.Bold))

        self.btm_play = QtWidgets.QPushButton(self)
        self.btm_play.move(230, 125)
        self.btm_play.setText("Играть")
        self.btm_play.setFixedWidth(115)

        self.btn_rule = QtWidgets.QPushButton(self)
        self.btn_rule.move(230, 175)
        self.btn_rule.setText("Правила")
        self.btn_rule.setFixedWidth(115)

def App():
    app = QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    App()
