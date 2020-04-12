"""
main.py
okenní apka
"""
from PyQt5 import QtWidgets
import sys

aplikace = QtWidgets.QApplication(sys.argv)         # vytvoření aplikace
formular = QtWidgets.QWidget()                      # vytvoření formuláře
boxlayout = QtWidgets.QHBoxLayout()

popisek = QtWidgets.QLabel("Ahoj Světe!", parent = formular)    # vložení textu do widgetu v parent
formular.setGeometry(500, 200, 400, 200)            # velikost okna

boxlayout.addStretch()          # vložení rozhahující se prázdného místa
boxlayout.addWidget(popisek)    # vložení popisku
boxlayout.addStretch()

formular.setLayout(boxlayout)
formular.setWindowTitle("Moje první aplikace v PyQt")
formular.show()                                     # zobrazení formuláře
sys.exit(aplikace.exec_())