"""
demoRadioButton.py
"""
from PyQt5 import QtWidgets, uic

class MyForm(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoRadioButton.ui", self)
        self.dialog.radioButton_FirstClass.toggled.connect(self.dispFare)
        self.dialog.radioButton_BusinessClass.toggled.connect(self.dispFare)
        self.dialog.radioButton_EconomyClass.toggled.connect(self.dispFare)
        self.show()

    def dispFare(self):
        fare = 0
        if self.dialog.radioButton_FirstClass.isChecked() == True:
            fare = 150
        if self.dialog.radioButton_BusinessClass.isChecked() == True:
            fare = 125
        if self.dialog.radioButton_EconomyClass.isChecked() == True:
            fare = 100
        self.dialog.labelFare.setText(f"Cena letenky je €{fare}")

def main():
    app = QtWidgets.QApplication([])
    _window = MyForm()
    app.exec()

main()