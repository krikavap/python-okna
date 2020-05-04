"""
callSignInForm.py
vyhledá uživatele podle emailové adresy zadané ve formuláři, ověří správnost hesla a zobrazí úspěch či neúspěch přihlášení 
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
        self.dialog = uic.loadUi("demoDatabase7.ui", self)    # načtení formuláře
        self.lineEditEmailAddress.setFocus()
        self.show()

    def SearchRows(self):
        """
        vyhledá uživatele v tabulce dle zadaného emailu a hesla. Pokud nenajde, zobrazí chybovou zprávu.
        """
        dBName = "demoEcommerce.db"          # jméno db
        tblName = "users"            # jméno tabulky
        email = self.lineEditEmailAddress.text()           # email
        heslo = self.lineEditPassword.text()
        # dotaz - hledám jméno vyhovující kombinaci email a heslo
        sqlStatement = "SELECT name FROM \"" + tblName + "\" WHERE email LIKE \"" + email + "\" and password LIKE \"" + heslo + "\""
        try:
            conn = sqlite3.connect(dBName)      # připojení db
            cur = conn.cursor()                 # iniciace kurzoru
            cur.execute(sqlStatement)       # provedení dotazu
            row = cur.fetchone()            # row obsahuje výsledek dotazu - jeden řádek na pozici kurzoru
            if row:                         # pokud je uživatel nalezen
                self.labelResponse.setText(f"Your are welcome, {row[0]}!")              
                
            else:                           # když není
                self.labelResponse.setText("Sorry, Incorrect email address or password")
                
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