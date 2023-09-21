import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


def window():
    app = QApplication([])
    win = QWidget()
    win.setFixedSize(700,800)


    btn = QPushButton(win)
    btn.setText('Send')
    btn.move(100,100)
    label = QLabel(win)
    label.setText('Hello')
    label.move(100,100)

    win.show()
    app.exec_()


window()