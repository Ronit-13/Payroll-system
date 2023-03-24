import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='12345',database='employees')
cur = conn.cursor()

print('=========================WELCOME TO PAYROLL MANAGEMENT SYSTEM===============================')
import datetime as dt
print(dt.datetime.now())
print('1.REGISTER')
print()
print('2.LOGIN')
print()



n=int(input('enter your choice='))
print()

if n== 1:
     name=input('Enter a Username=')
     print()
     passwd=int(input('Enter a 4 DIGIT Password='))
     print()
     V_SQLInsert="INSERT  INTO log_id (user_id,password) values (" +  str (passwd) + ",' " + name + " ') "
     cur.execute(V_SQLInsert)
     conn.commit()
     print()
     print('USER created succesfully')
     import main

if  n==2 :
     name=input('Enter your Username=')
     print()
     passwd=int(input('Enter your 4 DIGIT Password='))
     V_Sql_Sel="select * from log_id where password='"+str (passwd)+"' and user_id=  ' " +name+ " ' "
     cur.execute(V_Sql_Sel)
     if cur.fetchall() is  None:
          print()
          print('Invalid username or password')
     else:
          print()
          import main
