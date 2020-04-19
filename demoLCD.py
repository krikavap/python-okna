"""
demoLCD.py
"""

from PyQt5 import QtWidgets, uic, QtCore

class MyForm(QtWidgets.QDialog):
    """
    třída formuláře
    metoda prenes() přidá text do listu jako další položku
    metoda smaz() smaže vybranou položku z listu
    metoda smaz_vse() smaže celý list
    metoda edituj() umožní editaci vybrané položky listu
    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoLCD.ui", self)    # načtení formuláře
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showlcd)
        timer.start(1000)
        self.showlcd()
        self.show()

    def showlcd(self):
        time = QtCore.QTime.currentTime()
        text = time.toString("hh:mm:ss")
        self.lcdNumber.display(text)

def main():
    app = QtWidgets.QApplication([])
    _window = MyForm()
    app.exec()

main()