"""
demoColorChooseDialog.py
"""
from PyQt5.QtWidgets import QDialog, QApplication, QColorDialog 
from PyQt5 import uic
from PyQt5.QtGui import QColor
#from PyQt5.QtGui import QColor



class MyForm(QDialog):
    """
    třída formuláře
    formulář je včetně connection na pushButton nadefinován v ui souboru
    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoColorChooseDialog.ui", self)    # načtení formuláře
        col = QColor(0,0,0)         # init barva je černá
        self.widget.setStyleSheet("QWidget {background-color: %s }" % col.name())
        self.show()

    def disp_color(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.widget.setStyleSheet("QWidget {background-color: %s }" % col.name())
            self.label.setText(f"Vybral jsi barvu s kódem: {col.name()}")

def main():
    app = QApplication([])
    _window = MyForm()
    app.exec()

main()