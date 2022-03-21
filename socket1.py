#socket
#0-65525 total port
#0-1024 reserved for system
#TCP/IP
import socket
print(socket.gethostname())
host=input('Enter name')
print(socket.gethostbyname(host))