"""
travnik.py
"""
from PyQt5 import QtWidgets, uic, QtCore, QtGui, QtSvg
import numpy


cell_size = 32 # velikost buňky

# načtení obrázků trávy a zdi jako objektů
SVG_GRASS = QtSvg.QSvgRenderer("grass.svg")
SVG_WALL = QtSvg.QSvgRenderer("wall.svg")
SVG_WATTER = QtSvg.QSvgRenderer("watter.svg")
SVG_CASTLE = QtSvg.QSvgRenderer("castle.svg")

class GridWidget(QtWidgets.QWidget):
    """
    třída definující grid, do kterého se kreslí
    """
    def __init__(self, array):
        super().__init__()  # voláme konstruktor předka
        self.array = array
        # nastavíme velikost podle velikosti matice, jinak je náš objekt moc malý
        size = self.logical_to_pixels(*array.shape)
        self.setMinimumSize(*size)
        self.setMaximumSize(*size)
        self.resize(*size)

    def pixels_to_logical(self, x,y):
        return y//cell_size, x//cell_size

    def logical_to_pixels(self, row, column):
        return column * cell_size, row * cell_size

    def paintEvent(self, event):        # metoda je volána kdykoli např. OS požádá o překleslení okna (takže i po příkazu window.show() app.exec())
        rect = event.rect()  # získáme informace o překreslované oblasti

        # zjistíme, jakou oblast naší matice to představuje
        # nesmíme se přitom dostat z matice ven
        row_min, col_min = self.pixels_to_logical(rect.left(), rect.top())
        row_min = max(row_min, 0)
        col_min = max(col_min, 0)
        row_max, col_max = self.pixels_to_logical(rect.right(), rect.bottom())
        row_max = min(row_max + 1, self.array.shape[0])
        col_max = min(col_max + 1, self.array.shape[1])

        painter = QtGui.QPainter(self)  # budeme kreslit - metoda QPainter z knihovny QtGui

        for row in range(row_min, row_max):
            for column in range(col_min, col_max):
                # získáme čtvereček, který budeme vybarvovat
                x, y = self.logical_to_pixels(row, column)
                rect = QtCore.QRectF(x, y, cell_size, cell_size)
                
                # trávu dáme všude, protože i zdi stojí na trávě
                # zdi tam, kam patří
                if self.array[row, column] < 0:
                    SVG_GRASS.render(painter, rect)
                    SVG_WALL.render(painter, rect)
                elif self.array[row, column] == 0:
                    SVG_GRASS.render(painter, rect)
                elif self.array[row, column] == 1:
                    SVG_GRASS.render(painter, rect)
                    SVG_WATTER.render(painter, rect)
                elif self.array[row, column] == 2:
                    SVG_GRASS.render(painter, rect)
                    SVG_CASTLE.render(painter, rect)

    def mousePressEvent(self, event):
        # převedeme klik na souřadnice matice
        row, column = self.pixels_to_logical(event.x(), event.y())

        # Pokud jsme v matici, aktualizujeme data
        if 0 <= row < self.array.shape[0] and 0 <= column < self.array.shape[1]:
            self.array[row, column] = self.selected

            # tímto zajistíme překreslení widgetu v místě změny:
            # (pro Python 3.4 a nižší volejte jen self.update() bez argumentů)
            self.update(*self.logical_to_pixels(row, column), cell_size, cell_size)
     
class MyWindow(QtWidgets.QMainWindow):
    """ 
    definice hlavního okna aplikace
    """
    def __init__(self):
        super(MyWindow, self).__init__()
        window = uic.loadUi("travnik.ui", self)
        self.grid_preparation(window)
        self.palette_preparation(window)
        window.show()
        
    def grid_preparation(self, window):
        # připraví pole pro grid a inicializuje jej a naplní jej do oblasti scroll_area v hlavním okně
        array = numpy.zeros((15,20), dtype=numpy.int8)      # vytvoření pole nul
        array[:, 5] = -1                                    # nějaká zeď reprezentovaná -1
        # získáme oblast s posuvníky z Qt designeru
        self.scroll_area = window.findChild(QtWidgets.QScrollArea, "scrollArea")     # namapování na ui
        # dáme do ní náš grid
        self.grid = GridWidget(array)   # iniciace gridu
        self.scroll_area.setWidget(self.grid)       # přiřazení gridu do scroll_area

    def palette_preparation(self, window):
        # iniciuje paletu a nastaví ukazatel na první nástroj palety
        self.palette = window.findChild(QtWidgets.QListWidget,"palette")
        self.palette.setCurrentRow(0)

    def zmena(self):
        # odchytává změnu nástroje v paletě. událost je nastavena v návrhu okna Qt Designeru
        self.grid.selected = self.palette.currentRow()-1
        
def main():
    app = QtWidgets.QApplication([])
    window = MyWindow()
    app.exec()

main()