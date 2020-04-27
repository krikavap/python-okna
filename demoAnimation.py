"""
demoAnimation.py
zobrazí padající předmět po stisku tlačítka
využívá QPropertyAnimation class

"""
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QRect, QPropertyAnimation

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoAnimation1.ui", self)    # načtení formuláře
        self.show()

    def startAnimation(self):
        self.anim = QPropertyAnimation(self.labelPic, b"geometry")  # vytvoření objektu třídy QPropertyAnimation
        self.anim.setDuration(1000)         # prodlevy při animaci
        self.anim.setStartValue(QRect(270,30,80,80))        # startovní pozice
        self.anim.setEndValue(QRect(270, 30, 1020, 1020))     # koncová pozice
        self.anim.start()           # start animace
def main():
    app = QApplication([])
    _window = Window()
    app.exec()

main()