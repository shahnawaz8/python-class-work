#Client
from socket import *
s=socket()
port=5000
s.connect(('localhost',port))
print(s.recv(1024).decode())
s.close()
