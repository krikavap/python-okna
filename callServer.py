"""
callServer.py
server k callClient.py
vzájemně naváží síťové spojení a komunikují spolu
je tam nějaká chyba, která ale umožňuje funkci

"""
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5 import QtCore 
from PyQt5.QtCore import QCoreApplication
import socket
from threading import Thread
from socketserver import ThreadingMixIn
conn = None


class Window(QDialog):
    """
    třída formuláře
    formulář je včetně connection na pushButton nadefinován v ui souboru
    """
    def __init__(self):
        super().__init__()
        self.dialog = uic.loadUi("demoServer.ui", self)    # načtení formuláře
        self.textEditMessage = self.dialog.textEditMessage
        self.show()

    def send_text(self):
        text = self.lineEditMessage.text()
        global conn
        conn.send(text.encode("utf-8"))
        self.textEditMessage.append("Server: "+self.lineEditMessage.text())
        self.lineEditMessage.setText(" ")

class ServerThread(Thread):
    def __init__(self, window):
        super().__init__()
        self.window = window

    def run(self):
        TCP_IP = "127.0.0.1"
        TCP_PORT = 5555
        BUFFER_SIZE = 1024
        # vytvoří server socket
        tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        # připojí socket k adrese a portu
        tcpServer.bind((TCP_IP, TCP_PORT))
        threads = []
        # nastaví čekání na připojení (4 je délka fronty čekajících klientů)
        tcpServer.listen(4)
        while True:
            global conn
            conn, (ip, port) = tcpServer.accept()
            print("mám connection from",ip)
            #conn.send(b"dekuji za pripojeni")
            newthread = ClientThread(ip, port, self.window)
            newthread.start()
            threads.append(newthread)
        for t in threads:
            t.join()
        #conn.close()
        
class ClientThread(Thread):
    def __init__(self, ip, port, window):
        super().__init__()
        self.window = window
        self.ip = ip
        self.port = port

    def run(self):
        while True:
            global conn
            data = conn.recv(1024)
            self.window.textEditMessage.append('Client: '+data.decode('utf-8'))

def main():
    app = QApplication([])
    _window = Window()
    serverThread = ServerThread(_window)
    serverThread.start()
    app.exec()

main()