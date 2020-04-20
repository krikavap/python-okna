"""
demoMultilevelInheritance.py
demo multilevelové dědičnosti
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
        super().__init__(code, name)
        self.historyMarks = historyMarks
        self.geographyMarks = geographyMarks

    def getHistoryMarks(self):
        return self.historyMarks

    def getGeographyMarks(self):
        return self.geographyMarks

class Result(Marks):
    """
    dědičná třída třídy Marks
    atributy - totalMarks a percentage
    metody:
    getTotalMarks() - vrátí součet bodů zkoušek
    getPercentage() - vrátí procento úspěšnosti (maximum 100 pro každou zkoušku, tj. při dvou zkouškách to je 200 jako max)
    """
    def __init__(self, code, name, historyMarks, geographyMarks):
        super().__init__(code, name, historyMarks, geographyMarks)
        self.totalMarks = float(historyMarks) + float(geographyMarks)
        self.percentage = self.totalMarks / 200 * 100

    def getTotalMarks(self):
        return str(self.totalMarks)

    def getPercentage(self):
        return str(self.percentage)

class MyForm(QtWidgets.QDialog):
    """
    třída formuláře
    formulář je včetně connection na pushButton nadefinován v ui souboru
    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoMultilevelInheritance.ui", self)    # načtení formuláře
        self.show()

    def disp_message(self):
        # vytvoří instanci třídy Marks
        resultObj = Result(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text())
        # vypíše výsledek v label_total a label_perc
        self.label_total.setText(f"{resultObj.getTotalMarks()} bodů")
        self.label_perc.setText(f"{resultObj.getPercentage()} %")

def main():
    app = QtWidgets.QApplication([])
    _window = MyForm()
    app.exec()

main()