import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLineEdit,
    QLabel,
    QVBoxLayout
)

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.zikrlar = ('Subhan Alloh', 'Alhamdulillah', 'Allohu Akbar')
        self.count_zikr = 0

        self.v_box = QVBoxLayout() 

        self.label_zikr = QLabel(self.zikrlar[0])
        self.edit_count = QLineEdit('0')
        self.btn_count = QPushButton('📿')

        self.v_box.addWidget(self.label_zikr)
        self.v_box.addWidget(self.edit_count)
        self.v_box.addWidget(self.btn_count)

        self.setLayout(self.v_box)
    
        self.btn_count.clicked.connect(self.on_press)
        
    def on_press(self):
        count = int(self.edit_count.text())
        if count == 33:
            self.count_zikr += 1
            self.label_zikr.setText(self.zikrlar[self.count_zikr%3])
            count = -1
        self.edit_count.setText(str(count+1))
        

app = QApplication(sys.argv)
win = Window()
win.show()
app.exec_()
