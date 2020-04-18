"""
demoListWidget3.py
do textového pole umožní zadat novou položku listu a po stisku tlačítka ji přenese na konec listu
v listu je možné vybrat položku a pomocí tlačítka ji smazat
metoda prenes() přidá text do listu jako další položku
metoda smaz() smaže vybranou položku z listu
metoda smaz_vse() smaže celý list
metoda edituj() umožní editaci vybrané položky listu
connection je vytvořena přímo ve formuláři (návázání na metodu prenes() a smaz())
"""
from PyQt5 import QtWidgets, uic




class MyForm(QtWidgets.QDialog):
    """
    třída formuláře
    metoda prenes() přidá text do listu jako další položku
    metoda smaz() smaže vybranou položku z listu
    metoda smaz_vse() smaže celý list
    metoda edituj() umožní editaci vybrané položky listu
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

    def smaz_vse(self):
        """
        smaže všechny položky z list Widgetu
        """
        self.listWidget.clear()

    def edituj(self):
        """ 
        umožní editaci názvu položky v seznamu
        """
        _vybrany_radek = self.listWidget.currentItem().text()
        dialog = NewDialog(_vybrany_radek)
        if dialog.novy_text != "":
            self.listWidget.currentItem().setText(dialog.novy_text)
        
class NewDialog(QtWidgets.QDialog):
    """
    pomocný dialog pro změnu názvu položky v listu
    argument radek předává text původní položky v listu, která se má editovat
    """
    def __init__(self, radek):
        super().__init__()
        self.dialog = uic.loadUi("demoListWidget3-input.ui", self)    # načtení formuláře
        self.lineEdit.setText(radek)
        self.lineEdit.setFocus()
        self.lineEdit.selectAll()
        self.novy_text = ""
        _result = self.dialog.exec()

    def accept(self):
        super().accept()
        self.novy_text = self.lineEdit.text()

def main():
    app = QtWidgets.QApplication([])
    _window = MyForm()
    app.exec()

main()