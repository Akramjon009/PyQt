import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__Init()


    def __Init(self):
        self.setWindowTitle('Button')
        self.setFixedSize(400,300)

        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.btn1 = QPushButton("btn 1")
        self.btn2 = QPushButton("btn 2")
        self.btn3 = QPushButton("btn 3")
        self.btn4 = QPushButton("btn 4")

        self.h_box.addWidget(self.btn2)
        self.h_box.addWidget(self.btn3)
       
        self.v_box.addLayout(self.h_box)
        self.v_box.addWidget(self.btn1)
        self.v_box.addWidget(self.btn4)

        self.setLayout(self.v_box)

app = QApplication(sys.argv)
win = Window()
win.show()
app.exec_()