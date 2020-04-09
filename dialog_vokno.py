"""
dialog_vokno.py
"""
import sys
from PyQt5 import  QtCore, QtGui, QtWidgets
from Ui_dialog_tutorial import Ui_Dialog    # import class Ui_Dialog ze souboru Ui_dialog_tutorial.py

class MyDialog(QtWidgets.QDialog):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.ui = Ui_Dialog()       # přiřazení třídy U_Dialog
        self.ui.setupUi(self)       
        self.show()

    def say_hello(self, user_text):
        text = (f"Hello there, {user_text}!")
        self.ui.label_3.setText(text)

def main():
    app = QtWidgets.QApplication([])
    dialog = MyDialog()
    app.exec()

if __name__ == "__main__":
    main()