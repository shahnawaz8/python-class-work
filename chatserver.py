from socket import *
st=socket()

def server_program():
    port=5000
    host='localhost'
    st.bind((host,port))
    st.listen()
    print('Server is now Running')
    conn,address=st.accept()
    print("Connection from"+str(address))
    while True:
        data=conn.recv(1024).decode()
        if not data:
            break
        print("from Connected user:"+str(data))
        data=input('server>>')
        conn.send(data.encode())
    conn.close()
if __name__=='__main__':
    server_program()