from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
import random
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui  =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.vkdfjde22.clicked.connect(self.example)

    def example(self):
        signs = ''
        if self.ui.checkBox1.isChecked():
            signs = 'qwertyuiopasdfghjklzxcvbnm'
        if self.ui.checkBox_22.isChecked():
            signs = '1234567890'

        result = ''
        number = random.randint(5,10)
        for i in range(number):
            result += random.choice(signs)

        self.ui.label_23.setText(result)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()