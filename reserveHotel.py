"""
reserveHotel.py
demo rezervační formulář hotelu
práce s Calendar widgetem, spinBoxy, comboBoxem a PushButtonem
"""

from PyQt5 import QtWidgets, uic

class MyForm(QtWidgets.QDialog):
    """
    třída formuláře
    událost stisknutí PushButtonu - pressed() je odchytávána ve formuláři
    a je navázána na metodu calculate_rent() v této třídě
    metody: 
    calculate_rent() 
    show_results()
    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("reserveHotel.ui", self)    # načtení formuláře
        self.price = 0
        self.pokoju = 1    
        self.show()

    def calculate_rent(self):
        """
        metoda calculate_rent() je aktivována po stisknutí PushButton ve formuláři
        connection je nastavena ve formuláři
        vypočítá cenu za pobyt dle údajů zadaných ve formuláři
        """
        sazba = 0       # iniciační sazba za pokoj

        # načtení zadaných údajů z formuláře
        self.date = self.calendarWidget.selectedDate()      # datum příjezdu
        self.days = self.spinBox_days.value()               # počet dnů pobytu
        self.person = self.spinBox_person.value()           # počet osob
        self.room_type = self.comboBox.currentText()        # vybraný typ pokoje

        if self.comboBox.currentIndex() == 0:           # pokud je vybrán SingleRoom
            sazba = 25
            pokoju = self.person                        # počet pokojů = počtu osob
            self.price = sazba * self.days * self.person
        elif self.comboBox.currentIndex() == 1:         # pokud je vybrán DoubleRoom
            sazba = 40
            if self.person % 2 > 0:                     # výpočet nutného počtu pokojů pro zadaný počet osob
                pokoju = self.person//2 + 1
            else:
                pokoju = self.person//2
            self.price = sazba * self.days * pokoju
        elif self.comboBox.currentIndex() == 2:         # pokud je vybrán Apartment
            sazba = 60
            if self.person % 4 > 0:                     # výpočet nutného počtu apartmánů, max. obsazenost apartmánu jsou 4 osoby
                pokoju = self.person//4 + 1
            else:
                pokoju = self.person//4
            self.price = sazba * self.days * pokoju

        self.pokoju = pokoju
        self.show_results()             # volání metody show_results() pro výpis výsledků ve formuláři

    def show_results(self):
        """
        metoda show_results() v několika labelech vypíše ve formuláři rekapitulaci zadání a vypočítanou cenu
        """
        text_datum = self.date
        text_datum = text_datum.toString("d.M.yyyy")
        text1 = "Summary and calculation:"
        text2 = (f"Arrival Date: {text_datum}, Days of Reservation: {self.days}, Number of Person: {self.person}") 
        text3 = (f"Room type: {self.room_type}, Number of rooms: {self.pokoju} ")
        text4 = (f"Room Rent Price: €{self.price}")
        
        self.label_summary1.setText(text1)
        self.label_summary2.setText(text2)
        self.label_summary3.setText(text3)
        self.label_result.setText(text4)

def main():
    app = QtWidgets.QApplication([])
    _window = MyForm()
    app.exec()

main()