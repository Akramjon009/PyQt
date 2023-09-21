from sys import argv
from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton
)

class window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.i = 0
        self.__Init()
    
    def __Init(self):
        self.setWindowTitle("My First Window")
        self.setFixedSize(400,300)

        self.user_name = QLabel(self)
        self.edit_name = QLineEdit(self)
        self.user_last_name = QLabel(self)
        self.edit_last_name = QLineEdit(self)
        self.user_phone = QLabel(self)
        self.edit_phone = QLineEdit(self)
        self.btn_add = QPushButton(self)

        self.edit_name.setPlaceholderText('Enter Name...')

        self.user_name.setText('First name')
        self.user_last_name.setText('Last name')
        self.user_phone.setText('Phone number')
        self.btn_add.setText("Add new contact")

        self.user_name.move(50,50)
        self.edit_name.move(125,45)
        self.user_last_name.move(50,100)
        self.edit_last_name.move(125,95)
        self.user_phone.move(50,150)
        self.edit_phone.move(150, 145)

        self.edit_last_name.clear()

        self.btn_add.move(50,200)
        self.btn_add.setMinimumWidth(240)


        self.btn_add.clicked.connect(self.save_data)

    def clear_display(self):
        self.edit_name.clear()
        self.edit_last_name.clear()
        self.edit_phone.clear()


    def save_data(self):
        fname = self.edit_name.text()
        lname = self.edit_last_name.text()
        phone_num = self.edit_phone.text()
        if self.i % 2:
            self.edit_name.show()
        else:
            self.edit_name.hide()
        self.i += 1
        print(fname,lname, phone_num)
        self.clear_display()


app = QApplication(argv)
print(app)
win = window()
win.show()
app.exec_()