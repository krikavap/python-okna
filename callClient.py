"""
callClient.py
klient k callServer.py
vzájemně naváží síťové spojení a komunikují spolu
je tam nějaká chyba, která ale umožňuje funkci
"""


from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic
import socket
from PyQt5 import QtCore 
from threading import Thread
from socketserver import ThreadingMixIn
tcpClientA=None

class Window(QDialog):
    """
    třída formuláře
    formulář je včetně connection na pushButton nadefinován v ui souboru
    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoClient.ui", self)    # načtení formuláře
        self.textEditMessage = self.dialog.textEditMessage
        self.show()

    def send_text(self):
        text = self.lineEditMessage.text()
        self.textEditMessage.append("Client: "+self.lineEditMessage.text())
        tcpClientA.send(text.encode())
        self.lineEditMessage.setText(" ")

class ClientThread(Thread):
    def __init__(self,window):
        Thread.__init__(self)
        self.window=window
    def run(self):
        host = "127.0.0.1"
        print("host = ",host)
        port = 5555
        BUFFER_SIZE = 1024
        global tcpClientA
        tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpClientA.connect((host, port))
        while True:
            data = tcpClientA.recv(BUFFER_SIZE)
            self.window.textEditMessage.append('Server: '+data.decode('utf-8'))
            tcpClientA.close()


def main():
    app = QApplication([])
    _window = Window()
    clientThread=ClientThread(_window)
    clientThread.start()
    app.exec()

main()