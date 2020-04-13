"""
demoRadioButton2.py
ukázka jednoduchého formuláře s třemi skupinami radio buttonů
connection je vytvořena přímo ve formuláři (návázání na metodu shrnuti())

"""
from PyQt5 import QtWidgets, uic

class MyForm(QtWidgets.QDialog):
    """
    třída formuláře
    metoda dispFare přiřadí cenu letu dle vybrané varianty cestování a cenu vypíše do labelu labelFare
    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoRadioButton2.ui", self)    # načtení formuláře
        self.show()

    def shrnuti(self):
        """ 
        přiřadí vybrané varianty do labelu labelShrnuti
        """
        zprava1, zprava2, zprava3, zprava = "","","",""
        if self.dialog.radioButtonVelikostL.isChecked() == True:
            zprava1 = "L"
        if self.dialog.radioButtonVelikostS.isChecked() == True:
            zprava1 = "S"
        if self.dialog.radioButtonVelikostM.isChecked() == True:
            zprava1 = "M"
        if self.dialog.radioButtonVelikostXL.isChecked() == True:
            zprava1 = "XL"

        if self.dialog.radioButtonOsobne.isChecked() == True:
            zprava2 = "osobní vyzvednutí na prodejně"
        if self.dialog.radioButtonPPL.isChecked() == True:
            zprava2 = "dopravu společností PPL"
        if self.dialog.radioButtonPosta.isChecked() == True:
            zprava2 = "doručení prostřednictvím České pošty"

        if self.dialog.radioButtonKarta.isChecked() == True:
            zprava3 = "platbu platební kartou"
        if self.dialog.radioButtonDobirka.isChecked() == True:
            zprava3 = "platbu formou dobírky při doručení zboží"
        if self.dialog.radioButtonPrevod.isChecked() == True:
            zprava3 = "platbu bankovním převodem"
        
        zprava = (f"Vybral jsi triko velikosti {zprava1}, {zprava3} a {zprava2}.")
        self.dialog.labelShrnuti.setText(zprava)

def main():
    app = QtWidgets.QApplication([])
    _window = MyForm()
    app.exec()

main()