"""
demoLCD.py
"""

from PyQt5 import QtWidgets, uic, QtCore

class MyForm(QtWidgets.QDialog):
    """
    třída formuláře
    metoda showlcd() zjistí aktuální čas systému a pošle jej k zobrazení na lcd
    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoLCD.ui", self)    # načtení formuláře
        timer = QtCore.QTimer(self)             # přiřazení objektu třídy QTimer
        timer.timeout.connect(self.showlcd)     # connect na metodu showlcd
        timer.start(1000)                       # pauza každých 1000 ms
        self.showlcd()
        self.show()

    def showlcd(self):
        """
        metoda showlcd() zjistí aktuální čas systému a pošle jej k zobrazení na lcd
        """
        time = QtCore.QTime.currentTime()
        text = time.toString("hh:mm:ss")
        self.lcdNumber.display(text)

def main():
    app = QtWidgets.QApplication([])
    _window = MyForm()
    app.exec()

main()