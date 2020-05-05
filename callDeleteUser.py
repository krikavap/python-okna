"""
callDeleteUser.py
vyhledá uživatele podle emailové adresy a hesla zadaného ve formuláři, 
a po potvrzení jej smaže z tabulky users 
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
        self.dialog = uic.loadUi("demoDatabase9.ui", self)    # načtení formuláře
        # skrytí otázky a pushButtonů vztahujících se k potvrzení vymazání
        self.labelSure.hide()
        self.pushButtonYes.hide()
        self.pushButtonNo.hide()
        self.lineEditEmailAddress.setFocus()
        self.show()

    def DeleteUser(self):
        pass
        """
        vyhledá uživatele v tabulce dle zadaného emailu a hesla. Pokud nenajde, zobrazí chybovou zprávu.
        pokud najde, zobrazí dotaz, zda opravdu chceme záznam smazat a potvrzovací buttony
        """
        self.dbName  = "demoEcommerce.db"          # jméno db
        self.tblName = "users"            # jméno tabulky
        self.email = self.lineEditEmailAddress.text()           # email
        self.heslo= self.lineEditPassword.text()
        
        # dotaz 1 - hledám jméno vyhovující kombinaci email a heslo
        sqlStatement = "SELECT * FROM \"" + self.tblName + "\" WHERE email LIKE \"" + self.email + "\" and password LIKE \"" + self.heslo+ "\""
        try:
            conn = sqlite3.connect(self.dbName )      # připojení db
            cur = conn.cursor()                 # iniciace kurzoru
            cur.execute(sqlStatement)       # provedení dotazu - vyhledání uživatele
            row = cur.fetchone()            # row obsahuje výsledek dotazu - jeden řádek na pozici kurzoru
            if row:                         # pokud je uživatel nalezen, otestuji shodnost nových hesel
                self.labelSure.show()
                self.pushButtonYes.show()
                self.pushButtonNo.show()
                self.name = row[1]
                self.labelSure.setText(f"Are you sure to delete user {self.name}?")
                self.labelResponse.setText(f"User {self.name} found")              
            else:                           # když není
                self.labelSure.hide()
                self.pushButtonYes.hide()
                self.pushButtonNo.hide()
                self.labelResponse.setText("Sorry, Incorrect email address or password")
                
        except Error as e:
            self.labelResponse.setText("Error in accessing user account")
        finally:
            conn.close()
        
    def ConfirmDelete(self):
        """
        metoda vyvolána po stisku potvrzovacího buttonu na smazání záznamu
        sestaví příkaz a smaže záznam. nakonec skryje potvrzovací tlačítka
        """
        deleteStatement = "DELETE FROM \"" + self.tblName + "\" WHERE email LIKE \"" + self.email + "\" and password LIKE \"" + self.heslo + "\""
        try:
            conn = sqlite3.connect(self.dbName )      # připojení db
            cur = conn.cursor()                 # iniciace kurzoru
            with conn:
                cur.execute(deleteStatement)       # smazání uživatele
                self.labelSure.hide()
                self.pushButtonYes.hide()
                self.pushButtonNo.hide()
                self.labelResponse.setText(f"User {self.name} successfully deleted ")
        except Error as e:
            self.labelResponse.setText(f"Error in deleting User {self.name} account ")
        finally:
            conn.close()

    def NoConfirmDelete(self):
        """
        v případě, že ve formuláři uživatel odpoví No na potvrzovací dotaz ke smazání, skryjí se potvrzovací tlačítka a hláška 
        a řízení se vrátí do formuláře
        """
        self.labelSure.hide()
        self.pushButtonYes.hide()
        self.pushButtonNo.hide()
        self.labelResponse.setText("User will be not delete")

def main():
    app = QApplication([])
    app.setStyle('Fusion')
    _window = MyForm()
    app.exec()

main()