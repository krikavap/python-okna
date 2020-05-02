"""
callCreateTable.py
prostřednictvím formuláře vytvoří novou tabulku se sloupci v existující db 
omezení 
- neumí modifikovat existující tabulku
- pokud tabulka pod stejným názvem již existuje, nepřepíše ji a nová tabulka se nevytvoří

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
        self.dialog = uic.loadUi("demoDatabase2.ui", self)    # načtení formuláře
        self.lineEditDBName.setFocus()
        self.text = ""
        self.tabledefinition = ""        # globální proměnná do které se vkládají sql příkazy definující tabulku
        self.show()

    def createTbl(self):
        """
        vytvoření tabulky s nadefinovanými sloupci z procedury addColmn()
        """
        try:
            conn = sqlite3.connect(self.dBName)
            self.label_result.setText(f"database {self.dBName} is connected")
            cur = conn.cursor()
            self.tabledefinition +=");"       # tzn. iterátor: self.tabledefinition = self.tabledefinition + ");" - dokončení výrazu pro vytvoření tabulky
            # test, zda tabulka již neexistuje - to je dobré!!!
            dotaz = "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='"+self.tblName+"';"
            cur.execute(dotaz)          # spuštění dotazu
            if cur.fetchone()[0] == 1:      # pokud tabulka existuje, nová ji nepřepíše a ukončí se connection
                self.label_result.setText(f"table {self.tblName} exists, new version will be not created")
                conn.close()
            else:                        # když neexistuje tabulka s daným jménem, vytvoří se
                cur.execute(self.tabledefinition)
                self.label_result.setText(f"table {self.tblName} is successfully created")
        except Error as e:
            self.label_result.setText(f"Error in creating {self.tblName} table")
        finally:
            conn.close()

    def addColmn(self):
        """
        definuje sloupce, které mají být v nové tabulce
        """
        self.dBName = self.lineEditDBName.text()+".db"          # jméno db
        self.tblName = self.lineEditTableName.text()            # jméno tabulky
        colName = self.lineEditColumnName.text()
        if self.tabledefinition == "":               # jedná - li se o první zadaný sloupec
            self.tabledefinition = "CREATE TABLE \""+self.tblName+"\"(\""+colName+"\" "+self.comboBox.itemText(self.comboBox.currentIndex())         # konstrukce dotazu k vytvoření tabulky
            self.lineEditColumnName.setText("")
            self.lineEditColumnName.setFocus()
            self.text = "Columns: "+ colName
        else:                                   # jedná - li se o další sloupce, přidají se do konstrukce dotazu
            self.tabledefinition+=", \""+colName+"\" "+self.comboBox.itemText(self.comboBox.currentIndex())
            self.lineEditColumnName.setText("")
            self.lineEditColumnName.setFocus()
            self.text = self.text + ", " + colName
        self.label_ColumnList.setText(self.text)
        
def main():
    
    app = QApplication([])
    _window = MyForm()
    app.exec()

main()