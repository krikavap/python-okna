"""
demoOpenStreetMap2.py
na zadané souřadnice vyhledá v db OpenStreetMap místo

"""
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog
from geopy.geocoders import Nominatim


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoOpenStreetMap2.ui", self)    # načtení formuláře
        self.show()
        
    def displayDetails(self):
        latitude = float(self.lineEditLatitude.text())      # šířka
        longitude = float(self.lineEditLongitude.text())    # délka
        souradnice = str(latitude)+","+str(longitude)       # vytvoření řetězce
        nom = Nominatim(user_agent = "moje_aplikace")
        n = nom.reverse(souradnice)
        self.label_address.setText(f"Adresa: {n.address} ")
        
def main():
    app = QApplication([])
    _window = Window()
    app.exec()

main()