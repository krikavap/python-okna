"""
demoProgressBar.py
demonstruje využití progressbaru
connection je vytvořena přímo ve formuláři (návázání na pushButtonu na metodu update_bar()
"""
from PyQt5 import QtWidgets, uic

class MyForm(QtWidgets.QDialog):
    """
    třída formuláře
    metoda update_bar() spustí proces vyplňování progress baru
    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoProgressBar.ui", self)    # načtení formuláře
        self.show()
    
    def update_bar(self):
        """
        proces vyplňování progress baru
        """
        x = 0
        self.label_2.setText("")    # vyčištění textu v label_2
        while x < 100:
            for i in range(1, 1000000):     # cyklus pro zpomalení výpočtu
                n = i
            x = x + 1
            self.progressBar.setValue(x)    # nastavení hodnoty 
        self.label_2.setText("Stahování je dokončeno")  # oznámení stavu

def main():
    app = QtWidgets.QApplication([])
    _window = MyForm()
    app.exec()

main()