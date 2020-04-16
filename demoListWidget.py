"""
demoListWidget.py
zobrazí několik hodnot v listu a po výběru jedné z nich její hodnotu vypíše do labelu 
connection je vytvořena přímo ve formuláři (návázání na metodu disp_sel_item())

"""
from PyQt5 import QtWidgets, uic

class MyForm(QtWidgets.QDialog):
    """
    třída obsahující ListWidget
    metoda disp_sel_item() uloží text vybrané položky z listu do labelu pod listem

    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoListWidget.ui", self)    # načtení formuláře
        self.show()

    def disp_sel_item(self):
        """
        text vybrané položky listu uloží do výstupního labelu
        """
        value = self.listWidget.currentItem().text()    # do value uloží text vybrané položky
        self.label_vystup.setText(f"Vybral jsi: {value} ")  # labelu přiřadí text value
    
def main():
    app = QtWidgets.QApplication([])
    _window = MyForm()
    app.exec()

main()