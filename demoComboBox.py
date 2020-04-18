"""
demoComboBox.py
umožní vybrat položku z comboBoxu
text položky vypíše v labelu pod comboBoxem
connection je vytvořena přímo ve formuláři (návázání na metodu prenes() a smaz())
"""
from PyQt5 import QtWidgets, uic

class MyForm(QtWidgets.QDialog):
    """
    třída formuláře
    metoda vystup() přenese vybraný text z comboBoxu do labelu pod boxem
    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoComboBox.ui", self)    # načtení formuláře
        
        self.show()
    
    def vystup(self):
        text = self.comboBox.currentText()
        self.label_2.setText(text)

        
def main():
    app = QtWidgets.QApplication([])
    _window = MyForm()
    app.exec()

main()