"""
demoListWidget3.py
do textového pole umožní zadat novou položku listu a po stisku tlačítka ji přenese na konec listu
v listu je možné vybrat položku a pomocí tlačítka ji smazat
metoda prenes() přidá text do listu jako další položku
metoda smaz() smaže vybranou položku z listu
connection je vytvořena přímo ve formuláři (návázání na metodu prenes() a smaz())

"""
import sys
from PyQt5 import QtWidgets, uic

class MyForm(QtWidgets.QDialog):
    """
    třída formuláře
    metoda prenes() přidá text do listu jako další položku
    metoda smaz() smaže vybranou položku z listu

    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoListWidget3.ui", self)    # načtení formuláře
        self.show()

    def prenes(self):
        """
        text zapsaný do lineEdit přenese do listu jako poslední položku
        """
        self.listWidget.addItem(self.lineEdit.text())       # přidá položku do listu
        self.lineEdit.setText("")           # pak smaže text z lineEdit
        self.lineEdit.setFocus()            # předá focus na lineEdit
        
    def smaz(self):
        """
        smaže vybranou položku z listWidget
        """
        vybrany_radek = self.listWidget.currentRow()
        self.listWidget.takeItem(vybrany_radek)

def main():
    app = QtWidgets.QApplication([])
    _window = MyForm()
    app.exec()

main()