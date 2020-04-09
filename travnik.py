"""
travnik.py
"""
from PyQt5 import QtWidgets, uic, QtCore, QtGui, QtSvg
import numpy


cell_size = 32 # velikost buňky
VALUE_ROLE = QtCore.Qt.UserRole

# načtení obrázků trávy a zdi jako objektů
SVG_GRASS = QtSvg.QSvgRenderer("grass.svg")
SVG_WALL = QtSvg.QSvgRenderer("wall.svg")

def pixels_to_logical(x,y):
    return y//cell_size, x//cell_size

def logical_to_pixels(row, column):
    return column * cell_size, row * cell_size

class GridWidget(QtWidgets.QWidget):
    def __init__(self, array):
        super().__init__()  # voláme konstruktor předka
        self.array = array
        # nastavíme velikost podle velikosti matice, jinak je náš objekt moc malý
        size = logical_to_pixels(*array.shape)
        self.setMinimumSize(*size)
        self.setMaximumSize(*size)
        self.resize(*size)

    def paintEvent(self, event):        # metoda je volána kdykoli např. OS požádá o překleslení okna (takže i po příkazu window.show() app.exec())
        rect = event.rect()  # získáme informace o překreslované oblasti

        # zjistíme, jakou oblast naší matice to představuje
        # nesmíme se přitom dostat z matice ven
        row_min, col_min = pixels_to_logical(rect.left(), rect.top())
        row_min = max(row_min, 0)
        col_min = max(col_min, 0)
        row_max, col_max = pixels_to_logical(rect.right(), rect.bottom())
        row_max = min(row_max + 1, self.array.shape[0])
        col_max = min(col_max + 1, self.array.shape[1])

        painter = QtGui.QPainter(self)  # budeme kreslit - metoda QPainter z knihovny QtGui

        for row in range(row_min, row_max):
            for column in range(col_min, col_max):
                # získáme čtvereček, který budeme vybarvovat
                x, y = logical_to_pixels(row, column)
                rect = QtCore.QRectF(x, y, cell_size, cell_size)
                
                # podkladová barva pro poloprůhledné obrázky
                white = QtGui.QColor(255,255,255)
                painter.fillRect(rect, QtGui.QBrush(white))

                # trávu dáme všude, protože i zdi stojí na trávě
                SVG_GRASS.render(painter, rect)
                # zdi tam, kam patří
                if self.array[row, column] < 0:
                    SVG_WALL.render(painter, rect)
                """

                # šedá pro zdi, zelená pro trávu
                if self.array[row, column] < 0:
                    color = QtGui.QColor(115, 115, 115)         # zeď
                else:
                    color = QtGui.QColor(0, 255, 0)             # tráva

                # vyplníme čtvereček barvou
                painter.fillRect(rect, QtGui.QBrush(color))
                """


def main():
    app = QtWidgets.QApplication([])

    window = QtWidgets.QMainWindow()
    with open("mainw.ui") as f:             # vložení ui z Qt designeru
        uic.loadUi(f, window)

    # zatím přímo v kódu

    array = numpy.zeros((15,20), dtype=numpy.int8)      # vytvoření pole nul
    array[:, 5] = -1                                    # nějaká zeď reprezentovaná -1

    # získáme oblast s posuvníky z Qt designeru
    scroll_area = window.findChild(QtWidgets.QScrollArea, "scrollArea")     # namapování na ui

    # dáme do ní náš grid
    grid = GridWidget(array)
    scroll_area.setWidget(grid)

    palette = window.findChild(QtWidgets.QListWidget,"palette")
    """
    # ruční zadání položek mimo Qt Designer
    item = QtWidgets.QListWidgetItem('Grass')  # vytvoříme položku
    icon = QtGui.QIcon('grass.svg')  # ikonu
    item.setIcon(icon)  # přiřadíme ikonu položce
    palette.addItem(item)  # přidáme položku do palety

    item = QtWidgets.QListWidgetItem('Wall')  # vytvoříme položku
    icon = QtGui.QIcon('wall.svg')  # ikonu
    item.setIcon(icon)  # přiřadíme ikonu položce
    palette.addItem(item)  # přidáme položku do palety
    """
    def item_activated():
        """ volá se, když uživatel zvolí položku"""
        # Položek může obecně být vybráno víc, ale v našem seznamu je to
        # zakázáno (v Designeru selectionMode=SingleSelection).
        # Projdeme "všechny vybrané položky", i když víme že bude max. jedna.
        for item in palette.selectedItems():
            #print(item.data(VALUE_ROLE))
            row_num = palette.indexFromItem(item).row()
            print(row_num)

    palette.itemSelectionChanged.connect(item_activated)
    window.show()
    return app.exec()


main()