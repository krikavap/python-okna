"""
demoMultipleInheritance.py
demo multiple dědičnosti
class Results je potomkem třídy Student a Marks
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

class Marks:
    """
    třída Marks 
    atributy - navíc historyMarks, geographyMarks
    metody
    getHistoryMarks() - vrátí počet bodů historie
    getGeographyMarks() - vrátí počet bodů zeměpis
    """
    historyMarks = 0
    geographyMarks = 0
    def __init__(self, historyMarks, geographyMarks):
        self.historyMarks = historyMarks
        self.geographyMarks = geographyMarks

    def getHistoryMarks(self):
        return self.historyMarks

    def getGeographyMarks(self):
        return self.geographyMarks

class Results(Student, Marks):
    """
    třída je dědicem třídy Marks a Student
    atributy - totalMarks a percentage
    metody:
    getTotalMarks() - vrátí součet bodů zkoušek
    getPercentage() - vrátí procento úspěšnosti (maximum 100 pro každou zkoušku, tj. při dvou zkouškách to je 200 jako max)
    """
    def __init__(self, code, name, historyMarks, geographyMarks):
        super().__init__(code, name)                    # napřed dědí __init__ třídy Student
        super().__init__(historyMarks,geographyMarks)       # pak dědí __init__ třídy Marks
        self.totalMarks = float(historyMarks) + float(geographyMarks)
        self.percentage = self.totalMarks / 200 * 100

    def getTotalMarks(self):
        return self.totalMarks

    def getPercentage(self):
        return self.percentage

class MyForm(QtWidgets.QDialog):
    """
    třída formuláře
    formulář je včetně connection na pushButton nadefinován v ui souboru
    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoMultipleInheritance.ui", self)    # načtení formuláře
        self.show()

    def disp_message(self):
        # vytvoří instanci třídy Marks
        resultsObj = Results(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text())
        # vypíše výsledek v label_total a label_perc
        self.label_total.setText(f"{resultsObj.getTotalMarks():.0f} bodů")
        self.label_perc.setText(f"{resultsObj.getPercentage():.2f} %")

def main():
    app = QtWidgets.QApplication([])
    _window = MyForm()
    app.exec()

main()