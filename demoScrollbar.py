"""
demoScrollbar.py
ukázka jednoduché kalkulačkyformuláře s dvěmi line Edit poli. Hodnota z jednoho pole se pomocí 
tlačítek Kopíruj a Vlož překopíruje do druhého pole
connection je vytvořena přímo ve formuláři (návázání na standardní metody selectAll(), copy(), paste())

"""
from PyQt5 import QtWidgets, uic

class MyForm(QtWidgets.QDialog):
    """
    třída formuláře
    využívá standardní metody třídy QDialog pro výběr, kopírování a vložení textu
    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoScrollbar.ui", self)    # načtení formuláře
        self.show()

    def scrollhorizontal(self):
        #self.lineEditResult.setText(f"Sugar Level: {str(value)} ")
        value = self.dialog.horizontalScrollBarSugarLevel.value()
        self.lineEditResult.setText(f"Sugar Level: {value} ")
    def sliderhorizontal(self):
        value = self.dialog.horizontalSliderBloodPressure.value()
        self.lineEditResult.setText(f"Blood Pressure: {value} ")

    def scrollvertical(self):
        value = self.dialog.verticalScrollBarPulseRate.value()
        self.lineEditResult.setText(f"Pulse Rate: {value} ")

    def slidervertical(self):
        value = self.dialog.verticalSliderCholestrolLevel.value()
        self.lineEditResult.setText(f"Cholestrol Level: {value} ")


def main():
    app = QtWidgets.QApplication([])
    _window = MyForm()
    app.exec()

main()