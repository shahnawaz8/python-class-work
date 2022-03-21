from socket import *
s=socket()
host=gethostname()
port=5000
s.bind(('',port))
s.listen()
print('Server Program Started')
con,address=s.accept()
mes='Thanks for connection'
mes=str.encode(mes)
con.send(mes)
#con.close