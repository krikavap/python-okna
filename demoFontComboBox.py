"""
demoFontComboBox.py
umožní vybrat font z comboBoxu a tímto fontem je možné psát text v oblasti pod comboBoxem
connection je vytvořena přímo ve formuláři (návázání na metodu pis())
"""
from PyQt5 import QtWidgets, uic

class MyForm(QtWidgets.QDialog):
    """
    třída formuláře
    metoda pis() přenese vybraný font z comboBoxu do oblasti textedit
    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoFontComboBox.ui", self)    # načtení formuláře
        self.show()
    
    def pis(self):
        """
        vybraný font nastaví v edit text boxu
        """
        vybrany_font = self.fontComboBox.currentFont()
        self.textEdit.setFocus()
        self.textEdit.setCurrentFont(vybrany_font)
        
def main():
    app = QtWidgets.QApplication([])
    _window = MyForm()
    app.exec()

main()