from pymysql import *

while True:
    pas1=input('login id')
    pas2=input('Passwrd')
    conn=connect(db='employ',user='root',password='',host='localhost')
    cur=conn.cursor()
    query="SELECT * FROM `employee` WHERE E_id = ? and E_password= ? "
    cur.execute(query,[(pas1),(pas2)])
    conn.commit()
    conn.close()    
    new=cur.fetchall()
    print(new)
