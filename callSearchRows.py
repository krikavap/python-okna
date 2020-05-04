"""
callSearchRows.py
vyhledá uživatele podle emailové adresy zadané ve formuláři a zobrazí jeho heslo 
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
        self.dialog = uic.loadUi("demoDatabase6.ui", self)    # načtení formuláře
        self.lineEditDBName.setFocus()
        self.show()

    def SearchRows(self):
        """
        vyhledá uživatele v tabulce dle zadaného emailu
        """
        dBName = self.lineEditDBName.text()+".db"          # jméno db
        tblName = self.lineEditTableName.text()            # jméno tabulky
        email = self.lineEditEmailAddress.text()           # email
        sqlStatement = "SELECT password FROM \"" + tblName + "\" WHERE email LIKE \"" + email + "\""
        try:
            conn = sqlite3.connect(dBName)      # připojení db
            cur = conn.cursor()                 # iniciace kurzoru
            cur.execute(sqlStatement)       # provedení dotazu
            row = cur.fetchone()            # row obsahuje výsledek dotazu - jeden řádek na pozici kurzoru
            if row:                         # pokud je uživatel nalezen
                self.labelResponse.setText("Email Address Found, Password of this User is: ")              
                self.lineEditPassword.setText(row[0])           # heslo v otevřené formě
            else:                           # když není
                self.labelResponse.setText("Sorry, No User found with this Email Address")
                self.lineEditPassword.setText("")                                      
        except Error as e:
            self.labelResponse.setText("Error in accessing row")
        finally:
            conn.close()

def main():
    app = QApplication([])
    app.setStyle('Fusion')
    _window = MyForm()
    app.exec()

main()