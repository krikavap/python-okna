"""
demoOpenStreetMap1.py
zobrazí míč po stisku tlačítka pohybující se po křivce
využívá QPropertyAnimation class

"""
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog
from geopy.geocoders import Nominatim


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoOpenStreetMap1.ui", self)    # načtení formuláře
        self.show()
        
    def displayDetails(self):
        place = str(self.lineEditLocation.text())
        nom = Nominatim(user_agent = "moje_aplikace")
        n = nom.geocode(place)
        self.label_address.setText(f"Adresa: {n.address} ")
        self.label_longitude.setText(f"Zeměpisná délka: {n.longitude} ")
        self.label_latitude.setText(f"Zeměpisná šířka: {n.latitude} ")
        
def main():
    app = QApplication([])
    _window = Window()
    app.exec()

main()