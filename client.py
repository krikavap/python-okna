"""
jednoduchá síťová komunikace
klientská část
"""

import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = '127.0.0.1' 
port = 5555 
try: 
    s.bind((host, port)) 
except socket.error as e: 
    print(str(e)) 
    s.connect((host, port)) 
    print(s.recv(1024)) 
s.close()

