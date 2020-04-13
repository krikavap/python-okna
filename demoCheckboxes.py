"""
demoCheckboxes.py
ukázka jednoduchého formuláře se dvěma skupinami checkboxů a jednou skupinou radio buttonů
connection je vytvořena přímo ve formuláři (návázání na metodu recap())

"""
from PyQt5 import QtWidgets, uic

class MyForm(QtWidgets.QDialog):
    """
    třída formuláře
    metoda dispFare přiřadí cenu letu dle vybrané varianty cestování a cenu vypíše do labelu labelFare
    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoCheckboxes.ui", self)    # načtení formuláře
        self.show()

    def recap(self):
        """ 
        přiřadí vybrané varianty do labelu label_cena
        """
        cena = 0
        zprava = ""
        if self.dialog.radioButton.isChecked() == True:
            cena = cena + 75
        if self.dialog.radioButton_2.isChecked() == True:
            cena = cena + 85
        if self.dialog.radioButton_3.isChecked() == True:
            cena = cena + 110
        if self.dialog.radioButton_4.isChecked() == True:
            cena = cena + 95

        if self.dialog.checkBox.isChecked() == True:
            cena = cena + 10
        if self.dialog.checkBox_2.isChecked() == True:
            cena = cena + 15
        if self.dialog.checkBox_3.isChecked() == True:
            cena = cena + 15

        if self.dialog.checkBox_6.isChecked() == True:
            cena = cena + 35
        if self.dialog.checkBox_7.isChecked() == True:
            cena = cena + 30
        if self.dialog.checkBox_8.isChecked() == True:
            cena = cena + 15

        zprava = (f"Celková cena tvé objednávky je {cena} Kč.")
        self.dialog.label_cena.setText(zprava)

def main():
    app = QtWidgets.QApplication([])
    _window = MyForm()
    app.exec()

main()