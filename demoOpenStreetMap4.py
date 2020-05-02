"""
demoOpenStreetMap4.py
zobrazí vybrané místo v OpenStreetMap

"""
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog
# from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoOpenStreetMap4.ui", self)    # načtení formuláře
        self.show()
        
    def displayDetails(self):
        """
        spuštěna událostí stisk tlačítka ve formuláři
        řídí výpočet gps koordinátů a zobrazení mapy
        v okně aplikace demoOpenStreetMap4.ui musí být (a je) promotována třída QWidget widget to the QWebEngineView class
        """
        kam = str(self.lineEditURL.text())
        kam_address, kam_latitude, kam_longitude = self.coordinates(kam)    # zjištění koordinátů cíle
        self.goToHtml(kam_latitude, kam_longitude)      # volá metodu zobrazení mapy
       
    def coordinates(self, place):
        """
        vrátí GPS souřadnice místa 
        argument místo
        návratové hodnoty adresa, zeměpisná šířka, zeměpisná délka
        """
        nom = Nominatim(user_agent = "moje_aplikace")
        n = nom.geocode(place)
        return (n.address, n.latitude, n.longitude)

    def goToHtml(self, latitude, longitude):
        """
        zobrazí v okně aplikace openstreetmap se středem daným gps koordináty
        argumenty zeměpisná šířka, zeměpisná délka
        """
        gps_place = str(latitude)+"/"+str(longitude)
        link = "https://www.openstreetmap.org/#map=9/"+gps_place
        self.widget.load(QUrl(link))
   
def main():
    app = QApplication([])
    _window = Window()
    app.exec()

main()