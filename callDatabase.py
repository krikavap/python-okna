"""
callDatabase.py
vytvoří db sqlite3 se zadaným jménem
"""
import sqlite3
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic
from sqlite3 import Error


class MyForm(QDialog):
    """
    třída formuláře
    formulář je včetně connection na pushButton nadefinován v ui souboru
    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoDatabase1.ui", self)    # načtení formuláře
        self.show()

    def createDB(self):
        """
        vytvoří db se jménem, který uživatel zadá v dialogu
        """
        try:
            conn = sqlite3.connect(self.lineEditDBName.text()+".db")
            self.label_result.setText("Database is created")
        except Error as e:
            self.label_result.setText("Some error has occurred")
        finally:
            conn.close()
        
def main():
    app = QApplication([])
    _window = MyForm()
    app.exec()

main()