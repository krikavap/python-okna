"""
callInsertRowsInTable.py
prostřednictvím formuláře vytvoří nový řádek v tabulce
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
        self.dialog = uic.loadUi("demoDatabase3.ui", self)    # načtení formuláře
        self.lineEditDBName.setFocus()
        self.show()

    def InsertRows(self):
        """
        vytvoření nového řádku v tabulce. hodnoty jsou uživatelem zadány ve formuláři
        """
        dBName = self.lineEditDBName.text()+".db"          # jméno db
        tblName = self.lineEditTableName.text()            # jméno tabulky
        name = self.lineEditName.text()                    # jméno uživatele
        email = self.lineEditEmailAddress.text()           # email
        password = self.lineEditPassword.text()            # heslo

        # konstrukce sql příkazu
        sqlStatement = "INSERT INTO " + tblName + " (NAME, EMAIL, PASSWORD) VALUES (\"" + name + "\", \"" + email + "\", \"" + password + "\");"
        try:
            conn = sqlite3.connect(dBName)      # navázání spojení s db
            with conn:
                cur = conn.cursor()             # kurzor
                cur.execute(sqlStatement)          # spuštění dotazu
                self.labelResponse.setText("Row successfully inserted")
        except Error as e:
            self.labelResponse.setText(f"Error in inserting row")
        finally:
            conn.close()
  
def main():
    app = QApplication([])
    _window = MyForm()
    app.exec()

main()