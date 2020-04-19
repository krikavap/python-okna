"""
demoJednoduchaDedicnost.py
"""
from PyQt5 import QtWidgets, uic

class Student:
    """
    třída Student
    atributy code - kód, name - jméno
    metody
    getCode() - vrátí kód studenta
    getName() - vrátí jméno
    """
    name = ""
    code = ""
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def getCode(self):
        return self.code

    def getName(self):
        return self.name

class Marks(Student):
    """
    dědičná třída Marks třídy Student
    atributy - atributy Studenta a navíc historyMarks, geographyMarks
    metody
    getHistoryMarks() - vrátí počet bodů historie
    getGeographyMarks() - vrátí počet bodů zeměpis
    """
    historyMarks = 0
    geographyMarks = 0
    def __init__(self, code, name, historyMarks, geographyMarks):
        Student.__init__(self, code, name)
        self.historyMarks = historyMarks
        self.geographyMarks = geographyMarks

    def getHistoryMarks(self):
        return self.historyMarks

    def getGeographyMarks(self):
        return self.geographyMarks

class MyForm(QtWidgets.QDialog):
    """
    třída formuláře
    formulář je včetně connection na pushButton nadefinován v ui souboru
    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoJednoduchaDedicnost.ui", self)    # načtení formuláře
        self.show()

    def disp_message(self):
        # vytvoří instanci třídy Marks
        marksObj = Marks(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text())
        # vypíše v labelu_response
        self.label_response.setText(f"Jméno {marksObj.getName()}, kód {marksObj.getCode()}, \n body historie {marksObj.getHistoryMarks()}, body zeměpis {marksObj.getGeographyMarks()}")

def main():
    app = QtWidgets.QApplication([])
    _window = MyForm()
    app.exec()

main()