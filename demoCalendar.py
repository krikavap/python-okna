"""
demoCalendar.py
demo práce s Calendar widgetem
"""

from PyQt5 import QtWidgets, uic

class MyForm(QtWidgets.QDialog):
    """
    třída formuláře
    událost je odchytávána ve formuláři
    metoda show_date() je aktivována po změně data ve widgetu calendar
    a datum z widgetu calendar přenese do prvku dateEdit třídy QDateEdit
    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoCalendar.ui", self)    # načtení formuláře
        self.show()

    def show_date(self):
        """
        metoda show_date() je aktivována po změně data ve widgetu calendar
        a datum z widgetu calendar přenese do prvku dateEdit třídy QDateEdit
        """
        date = self.calendarWidget.selectedDate()
        self.dateEdit.setDate(date)

def main():
    app = QtWidgets.QApplication([])
    _window = MyForm()
    app.exec()

main()