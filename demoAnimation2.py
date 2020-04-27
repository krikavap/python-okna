"""
demoAnimation2.py
zobrazí padající a odrážející se míč po stisku tlačítka
využívá QPropertyAnimation class

"""
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QRect, QPropertyAnimation

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoAnimation2.ui", self)    # načtení formuláře
        self.show()

    def startAnimation(self):
        self.anim = QPropertyAnimation(self.labelPic, b"geometry")  # vytvoření objektu třídy QPropertyAnimation
        self.anim.setDuration(1000)         # prodlevy při animaci
        self.anim.setKeyValueAt(0, QRect(0,0,0,0))        # startovní pozice
        self.anim.setKeyValueAt(0.5, QRect(420,460,0,0))   
        self.anim.setKeyValueAt(1, QRect(850,0,0,0))   
       
       
        self.anim.start()           # start animace
def main():
    app = QApplication([])
    _window = Window()
    app.exec()

main()