"""
demoGraphicsView.py
zobrazí obrázek v Graphics View widgetu

"""
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap 

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoGraphicsView.ui", self)    # načtení formuláře
        self.scene = QGraphicsScene(self)   # vytvoření instance třídy QGraphicsScene()
        pixmap = QPixmap()                  # vytvoření instance třídy QPixmap() - vytvoří reprezentaci offline obrázku
        pixmap.load("pf2015.jpg")           # načtení obrázku do objektu
        item = QGraphicsPixmapItem(pixmap)  # vytvoří objekt, který se může jako položka přidat do scény
        self.scene.addItem(item)            # přidání do scény
        # přidání dalšího obrázku
        pixmap.load("wall.svg")
        item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)

        # zobrazení - přiřazení připravené scény do prvku graphicsView ve formuláři
        self.graphicsView.setScene(self.scene)
        self.show()

def main():
    app = QApplication([])
    _window = Window()
    app.exec()

main()