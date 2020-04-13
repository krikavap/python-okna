"""
demoRadioButton.py
ukázka jednoduchého formuláře s radio buttony
connection je vytvořena v druhé verzi přímo ve formuláři (návázání na metodu dispFare())

"""
from PyQt5 import QtWidgets, uic

class MyForm(QtWidgets.QDialog):
    """
    třída formuláře
    metoda dispFare přiřadí cenu letu dle vybrané varianty cestování a cenu vypíše do labelu labelFare
    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoRadioButton.ui", self)    # načtení formuláře
        #self.dialog.radioButton_FirstClass.toggled.connect(self.dispFare)
        #self.dialog.radioButton_BusinessClass.toggled.connect(self.dispFare)
        #self.dialog.radioButton_EconomyClass.toggled.connect(self.dispFare)
        self.show()

    def dispFare(self):
        """ 
        přiřadí cenu letu do labelFare
        """
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