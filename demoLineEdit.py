"""
demoLineEdit.py
ukázka jednoduchého formuláře s dvěmi line Edit poli. Hodnota z jednoho pole se pomocí 
tlačítek Kopíruj a Vlož překopíruje do druhého pole
connection je vytvořena přímo ve formuláři (návázání na standardní metody selectAll(), copy(), paste())

"""
from PyQt5 import QtWidgets, uic

class MyForm(QtWidgets.QDialog):
    """
    třída formuláře
    
    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoLineEdit.ui", self)    # načtení formuláře
        self.show()

def main():
    app = QtWidgets.QApplication([])
    _window = MyForm()
    app.exec()

main()