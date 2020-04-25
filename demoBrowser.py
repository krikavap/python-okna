"""
demoBrowser.py
jednoduchý html browser
"""
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class MyForm(QDialog):
    """
    třída formuláře
    formulář je včetně connection na pushButton nadefinován v ui souboru
    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoBrowser.ui", self)    # načtení formuláře
        self.show()

    def goToHtml(self):
        self.widget.load(QUrl(self.lineEditURL.text()))

def main():
    app = QApplication([])
    _window = MyForm()
    app.exec()

main()