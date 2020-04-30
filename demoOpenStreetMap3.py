"""
demoOpenStreetMap3.py
vypočítá vzdálenost mezi dvěmi lokalitami

"""
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoOpenStreetMap3.ui", self)    # načtení formuláře
        self.show()
        
    def displayDetails(self):
        """
        spuštěna událostí stisk tlačítka ve formuláři
        řídí výpočet a zobrazení výsledné vzdálenosti mezi zadanými místy
        """
        odkud = str(self.lineEditLocFrom.text())      # odkud - místo, adresa
        kam = str(self.lineEditLocTo.text())           # kam - místo, adresa 
        odkud_address, odkud_latitude, odkud_longitude = self.coordinates(odkud)    # zjištění koordinátů startu
        kam_address, kam_latitude, kam_longitude = self.coordinates(kam)    # zjištění koordinátů cíle
        # příprava dat
        odkud_gps = (odkud_latitude, odkud_longitude)
        kam_gps = (kam_latitude, kam_longitude)
        # výpočet vzdálenosti v km vzdušnou čarou prostřednictvím metody vzdálenost
        vzdalenost = self.vzdalenost(odkud_gps, kam_gps)
        # vypsání výsledku do okna aplikace
        self.label_distance.setText(f"Vzdálenost mezi: \n výchozím bodem: {odkud_address}\n a cílovým bodem: {kam_address} \n je {vzdalenost:10.3f} km vzdušnou čarou.")
        
    def coordinates(self, place):
        """
        vrátí GPS souřadnice místa 
        argument místo
        návratové hodnoty adresa, zeměpisná šířka, zeměpisná délka
        """
        nom = Nominatim(user_agent = "moje_aplikace")
        n = nom.geocode(place)
        return (n.address, n.latitude, n.longitude)

    def vzdalenost(self, odkud, kam):
        """ 
        metoda vrátí vzdálenost mezi dvěmi body v kilometrech
        argumenty odkud, kam, každý je tvořený dvojicí GPS souřadnic
        """
        return (geodesic(odkud, kam).km)
        
def main():
    app = QApplication([])
    _window = Window()
    app.exec()

main()