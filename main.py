from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog
from design import Ui_Form as Design
import sys


class Widget(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.now = None
        self.path = ''
        self.pushButton.clicked.connect(self.open_file)
        self.pushButton_2.clicked.connect(self.create_file)
        self.pushButton_3.clicked.connect(self.save_file)

    def open_file(self):
        try:
            a = QFileDialog.getOpenFileName()[0]
            self.path = a
            with open(a, 'r') as document:
                mad = document.readlines()
                for i in mad:
                    print(i)
                self.plainTextEdit.appendPlainText(f"{''.join(mad)}")
            self.pushButton_3.setEnabled(True)
        except:
            pass

    def create_file(self):
        self.now = ''''''
        self.plainTextEdit.setPlainText("")
        self.pushButton_3.setEnabled(True)

    def save_file(self):
        if type(self.now) == str:
            try:
                a = QFileDialog.getSaveFileName()[0]
                with open(a, 'w') as output:
                    output.write(self.plainTextEdit.toPlainText())
                    self.now = None
                    self.path = a
            except:
                pass
        else:
            with open(self.path, 'w') as output:
                output.write(self.plainTextEdit.toPlainText())


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())