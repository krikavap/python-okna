"""
demoAnimation3.py
zobrazí míč po stisku tlačítka pohybující se po křivce
využívá QPropertyAnimation class

"""
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QRect, QPropertyAnimation, QPointF, pyqtProperty
from PyQt5.QtGui import QPainter, QPainterPath

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoAnimation2.ui", self)    # načtení formuláře
        self.show()
        self.path = QPainterPath()
        self.path.moveTo(30,30)
        self.path.cubicTo(30,30,80,180,180,170)
        self.labelPic.pos = QPointF(20,20)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.drawPath(self.path)
        qp.end()
        

    def startAnimation(self):
        self.anim = QPropertyAnimation(self.labelPic, b"pos")  # vytvoření objektu třídy QPropertyAnimation
        self.anim.setDuration(4000)         # prodlevy při animaci
        self.anim.setStartValue(QPointF(20,20))
        positionValues = [n/80 for n in range(0,50)]
        
        for i in positionValues:
            self.anim.setKeyValueAt(i, self.path.pointAtPercent(i))
            self.anim.setEndValue(QPointF(160,150))        
            self.anim.start()
        
def main():
    app = QApplication([])
    _window = Window()
    app.exec()

main()