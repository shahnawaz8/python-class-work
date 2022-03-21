from socket import *
st=socket()
def client_program():
    host='localhost'
    port=5000
    st.connect((host,port))
    msg=input("Client>>")
    while msg.lower().strip()!='bye':
        st.send(msg.encode())
        data=st.recv(1024).decode()
        print('Receive From Server:'+data)
        msg=input('>>')
    st.close()
if __name__=='__main__':
    client_program()