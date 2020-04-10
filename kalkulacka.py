"""
kalkulacka.py
primitivní kalkulačka využívající formuláře vytvořeného v QtDesigneru
formulář má třídy QComboBox, QLabel, QLineEdit, QPushButton
TODO test, zda vstupní hodnoty jsou pouze platná čísla (nikoli text, či řetězce)
"""
from PyQt5 import uic, QtWidgets, QtGui


class Window(QtWidgets.QMainWindow):
    """
    třída okna aplikace
    """
    def __init__(self):
        """
        init procedura. dědí vlastnosti QtWidgets.QMainWindow
        přiřazuje výstup QtDesigneru 
        """
        super(Window, self).__init__() 
        okno = uic.loadUi("kalkulacka.ui", self)
        okno.show()
        self.volba="+"          # iniciace matematického operátora pro případ, že při prvním použití kalkulačky jej uživatel nevybere

    def say_hello(self):
        """
        odchytí stisknutí tlačítka vypočítej ve formuláři a zavolá metodu vypocet()
        """
        self.vypocet()
        
    def combo_change(self):
        """
        zaznamená změnu operátora ve formuláři a přiřadí operátor do proměnné self.volba
        """
        self.volba = self.comboBox.currentText()
        # print("combo"+self.volba)     # pro testování na konzoli vypíše zvolený operátor
    
    def vypocet(self):
        """
        vlastní výpočet dle zvoleného typu matematické operace
        """ 
        # otestování, zda jsou oba operátoři ve formuláři vyplněné a jsou čísla
        if self.lineEdit.text() == "": 
            text = "1. operátor musí být vyplněn a musí obsahovat číslo"
        elif self.lineEdit_2.text() == "":
            text = "2. operátor musí být vyplněn a musí obsahovat číslo"
        
        # pokud ano, testuje se typ zvolené operace
        else:           
            if self.volba == "+":
                vysledek= float(self.lineEdit.text()) + float(self.lineEdit_2.text())
                text = str(f"Výsledek je: {vysledek:.5f}")
            
            elif self.volba == "-":
                vysledek= float(self.lineEdit.text()) - float(self.lineEdit_2.text())
                text = str(f"Výsledek je: {vysledek:.5f}")
            
            elif self.volba == "*":
                vysledek= float(self.lineEdit.text()) * float(self.lineEdit_2.text())
                text = str(f"Výsledek je: {vysledek:.5f}")
            
            elif self.volba == "/":
                # druhý operátor nesmí být nula
                if float(self.lineEdit_2.text()) == 0:
                    text = "Nelze dělit nulou"
                else:
                    vysledek= float(self.lineEdit.text()) / float(self.lineEdit_2.text())
                    text = str(f"Výsledek je: {vysledek:.5f}")
            
            elif self.volba == "//":
                # druhý operátor nesmí být nula
                if float(self.lineEdit_2.text()) == 0:
                    text = "Nelze dělit nulou"
                else:
                    vysledek= float(self.lineEdit.text()) // float(self.lineEdit_2.text())
                    text = str(f"Výsledek je: {vysledek}")
            
            elif self.volba == "%":
                # druhý operátor nesmí být nula
                if float(self.lineEdit_2.text()) == 0:
                    text = "Nelze dělit nulou"
                else:
                    vysledek= float(self.lineEdit.text()) % float(self.lineEdit_2.text())
                    text = str(f"Výsledek je: {vysledek:.5f}")
            
        self.zprava(text)   # volá metodu vypisující zprávy do formuláře
    
    def zprava(self,text):
        """
        posílá texty předané argumentem do labelu_3 formuláře
        """
        self.label_3.setText(text)

def main():
    """
    hlavní řídící procedura
    """
    app = QtWidgets.QApplication([])
    window = Window()       # vytvoří instanci objektu
    app.exec()

if __name__ == "__main__":
    main()