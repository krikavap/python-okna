"""
demoListWidget2.py
zobrazí několik hodnot v listu a po výběru několika z nich jejich hodnoty vypíše do výstupního listu
connection je vytvořena přímo ve formuláři (návázání na metodu disp_sel_item())

"""
from PyQt5 import QtWidgets, uic

class MyForm(QtWidgets.QDialog):
    """
    formulář, který obsahuje 2 ListWidget
    metoda disp_sel_item() uloží text vybraných položek z listu do výstupního listu

    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoListWidget2.ui", self)    # načtení formuláře
        self.show()

    def disp_sel_item(self):
        """
        text vybraných položek listu uloží do výstupního listu
        """
        self.listWidget_2.clear()       # vyčistí výstupní list
        polozky = self.listWidget.selectedItems()           # načte položky, které byly vybrány
        for i in list(polozky):       
            self.listWidget_2.addItem(i.text())  # všechny položky vypíše ve výstupním listu
    
def main():
    app = QtWidgets.QApplication([])
    _window = MyForm()
    app.exec()

main()