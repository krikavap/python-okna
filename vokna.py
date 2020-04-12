"""
vokna.py
"""
from PyQt5 import QtWidgets
app = QtWidgets.QApplication([])

# hlavní okno
main = QtWidgets.QWidget()
main.setWindowTitle("Hello Qt")

# layout pro hlavní okno
layout = QtWidgets.QHBoxLayout()
main.setLayout(layout)

# nápis
label = QtWidgets.QLabel("Click the button to change me")
layout.addWidget(label)     # přidáním do layoutu se nápis stane automaticky potomkem hlavního okna

# tlačítko
button = QtWidgets.QPushButton("Click me")
layout.addWidget(button)

# funkcionalita
def change_label():
    label.setText("Good job. +100 points")
    

button.clicked.connect(change_label)
main.show()

"""
# combo box
box = QtWidgets.QComboBox()
box.addItem("First Option")
box.addItem("Second Option")

# základní varianta - napojí na activated - vrací int - číslo volby
# box.activated.connect(print)

# výběr varianty - první vrací text položky, druhý příkaz číslo volby
#box.activated[str].connect(print)
box.activated[int].connect(print)

box.show()
"""
"""
button = QtWidgets.QPushButton("Click to Exit")
button.setWindowTitle("Goodbye World")
button.clicked.connect(app.quit)

button.show()
"""
app.exec()
