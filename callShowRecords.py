"""
callShowRecords.py
ve formuláři jednotlivé řádky tabulky users. jednotlivými záznamy je možné listovat pomocí tlačítek
hesla se nezobrazují v otevřené formě -> na úrovni formuláře se zamění znaky za tečky (nastaveno v designu formuláře). 
v databázi jsou hesla uložena jako prostý text
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
        self.dialog = uic.loadUi("demoDatabase5.ui", self)    # načtení formuláře
        cur.execute(sqlStatement)           # spuštění iniciačního dotazu 
        self.show()

    def ShowFirstRow(self):
        """
        skok na první řádek tabulky
        """
        global rowNo
        rowNo = 1
        try:
            cur.execute(sqlStatement)       # dotaz iniciační
            row = cur.fetchone()            # row obsahuje jeden řádek na pozici kurzoru (je na prvním řádku)
            if row:                         # výpis hodnot do formuláře
                self.labelResponse.setText("")              
                self.lineEditName.setText(row[0])               # jméno
                self.lineEditEmailAddress.setText(row[1])       # email
                self.lineEditPassword.setText(row[2])           # heslo (zobrazí se jen jako tečky, nastaveno v designu formuláře)
        except Error as e:
            self.labelResponse.setText("Error in accessing table")
    
    def ShowLastRow(self):
        """
        skok na poslední řádek tabulky
        """
        global rowNo
        cur.execute(sqlStatement)               # dotaz iniciační - vrátí celou tabulku
        tab = cur.fetchall()
        pocet_zaznamu = len(tab)
        for row in tab:              # toto není úplně čisté a hlavně rychlé pro velké tabulky - prochází celou tabulku a postupně ji vypisuje do formuláře, až se zastaví na posledním záznamu
            self.labelResponse.setText("")              
            self.lineEditName.setText(row[0])               # jméno
            self.lineEditEmailAddress.setText(row[1])       # email
            self.lineEditPassword.setText(row[2])           # heslo (zobrazí se jen jako tečky, nastaveno v designu formuláře)
        rowNo = pocet_zaznamu
    
    def ShowNextRow(self):
        """
        skok na další řádek tabulky
        """
        global rowNo            # globální - mění ji metoda ShowNextRow() a ShowPreviousRow()
        rowNo = rowNo + 1
        sqlStatement = "SELECT name, email, password FROM users WHERE rowid = "+str(rowNo)
        cur.execute(sqlStatement)
        row = cur.fetchone()
        if row:
            self.labelResponse.setText("")              
            self.lineEditName.setText(row[0])               # jméno
            self.lineEditEmailAddress.setText(row[1])       # email
            self.lineEditPassword.setText(row[2])           # heslo (zobrazí se jen jako tečky, nastaveno v designu formuláře)
        else:       # když jsme na posledním řádku
            rowNo = rowNo - 1
            self.labelResponse.setText("This is the last row")

    def ShowPreviousRow(self):
        """
        skok na předchozí řádek tabulky
        """
        global rowNo
        rowNo = rowNo - 1
        sqlStatement = "SELECT name, email, password FROM users WHERE rowid = "+str(rowNo)
        cur.execute(sqlStatement)
        row = cur.fetchone()
        if row:
            self.labelResponse.setText("")              
            self.lineEditName.setText(row[0])               # jméno
            self.lineEditEmailAddress.setText(row[1])       # email
            self.lineEditPassword.setText(row[2])           # heslo (zobrazí se jen jako tečky, nastaveno v designu formuláře)
        else:       # když jsme na prvním řádku
            rowNo = rowNo + 1
            self.labelResponse.setText("This is the first row")

def main():
    app = QApplication([])
    app.setStyle('Fusion')
    _window = MyForm()
    app.exec()

# globální proměnné
rowNo = 1       # číslo řádku
sqlStatement = "SELECT name, email, password FROM users"        # iniciační dotaz
conn = sqlite3.connect("demoEcommerce.db")      # navázání spojení s db
cur = conn.cursor()                 # kurzor

main()