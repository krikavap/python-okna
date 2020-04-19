"""
demoTableWidget.py
"""
from PyQt5 import QtWidgets, uic
from QWidget import QTableWidgetItem

class MyForm(QtWidgets.QDialog):
    """
    třída formuláře
    metoda showlcd() zjistí aktuální čas systému a pošle jej k zobrazení na lcd
    """
    def __init__(self, data):
        super().__init__()
        self.dialog = uic.loadUi("demoTableWidget.ui", self)    # načtení formuláře
        self.data = data
        self.addcontent()       
        self.show()

    def addcontent(self):
        """
        metoda showlcd() zjistí aktuální čas systému a pošle jej k zobrazení na lcd
        """
        row = 0
        col = 0
        pocet_prvku = len(self.data)
        i = 0
        max_row = 3
        max_col = 2
        for row in range(0, max_row):
            for col in range(0, max_col):
                item = self.data[i]
                oneitem = QTableWidgetItem(str(item))
                self.tableWidget.setItem(row,col,oneitem)
                i = i + 1

def main():
    app = QtWidgets.QApplication([])
    data = ("Single Room", 25, "Double Room", 40, "Apartment", 60)
    _window = MyForm(data)
    app.exec()

main()