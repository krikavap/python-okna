"""
callDisplayRows.py
ve formuláři zobrazí obsah vybrané tabulky
"""
import sqlite3
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from PyQt5 import uic
from sqlite3 import Error

class MyForm(QDialog):
    """
    třída formuláře
    formulář je včetně connection na pushButton nadefinován v ui souboru
    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoDatabase4.ui", self)    # načtení formuláře
        self.lineEditDBName.setFocus()
        self.show()

    def DisplayRows(self):
        """
        zobrazení řádků tabulky ve formuláři
        """
        dBName = self.lineEditDBName.text()+".db"          # jméno db
        tblName = self.lineEditTableName.text()            # jméno tabulky
        # name = self.lineEditName.text()                    # jméno uživatele
        # email = self.lineEditEmailAddress.text()           # email
        # password = self.lineEditPassword.text()            # heslo

        # konstrukce sql příkazu
        sqlStatement = "SELECT * FROM " + tblName 
        try:
            conn = sqlite3.connect(dBName)      # navázání spojení s db
            with conn:
                cur = conn.cursor()             # kurzor
                cur.execute(sqlStatement)          # spuštění dotazu
                rows = cur.fetchall()
                rowNo = 0
                for tuple in rows:
                    self.labelResponse.setText("")
                    colNo = 0
                    for columns in tuple:
                        if columns != 0:
                            oneColumn = QTableWidgetItem(columns)
                            self.tableWidget.setItem(rowNo, colNo-1, oneColumn)
                        colNo = colNo + 1
                    rowNo = rowNo + 1
        except Error as e:
            self.tableWidget.clear()
            self.labelResponse.setText(f"Error in accessing table")
        finally:
            conn.close()
  
def main():
    app = QApplication([])
    app.setStyle('Fusion')
    _window = MyForm()
    app.exec()

main()