import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='12345',database='Payroll')
mycursor=conn.cursor()

   
def menu():
    c='yes'
    c=input("do you want to continue or not(yes or No):")
    print("          PAYROLL SYSTEM            ")
    while(c=='yes'):
        
        print()
        print("1.employee registeration")
        print("2.employee details")
        print("3.employees list")
        print("4.know the number of employees")
        print("5.Increment in salary(10%)")
        print("6.know your salary")
        print("exiting")
        choice=int(input("      enter the choice: "))
        
        if choice==1:
            register()
        elif choice==2:
            details()
        elif choice==3:
            em_list()
        elif choice==4:
            em_count()
        elif choice==5:
            em_salary()    
        elif choice==6:
            salary()
        else:
            print ("exit")
            break
    else : print("Thank You")
    
    
def register():
    import mysql.connector as sql
    conn=sql.connect(host='localhost',user='root',password='12345',database='Payroll')
    mycursor=conn.cursor()
    v_em_no=int(input("enter your employee ID: "))
    v_em_name=input ("enter your name: ")
    v_em_dept=input( "enter department you want to join: ") 
    v_em_age=int(input("enter your age: "))
    
    days = (float(input("Please enter days worked (In a month): ")))
    payrate = 4000
    if days <= 22:
        regularpay = (days * payrate)
        v_em_salary=regularpay
    elif days > 22:
        overtimehours = (days - 22.00)
        regularpay = (days * payrate)
        overtimerate = (payrate * 1.5)
        overtimepay = (overtimehours * overtimerate)
        grosspay = (regularpay+overtimepay)
        v_em_salary=grosspay

    v_sql_insert="insert into office values("+str(v_em_no)+",'" +v_em_name+"','"+v_em_dept+"',"+str(v_em_salary)+","+str(v_em_age)+")"
    mycursor.execute(v_sql_insert)
    conn.commit()
    print("congrats you have joined suuceessfully")
    print("       registerd suyccessfully          ")

    
def details():
    import mysql.connector as sql
    name=input('Enter your name: ')
    conn=sql.connect(host='localhost',user='root',password='12345',database='Payroll')
    mycursor=conn.cursor()
    mycursor.execute("select * from OFFICE where em_name= '"+ name +"'")
    results=mycursor.fetchall()
    conn.commit()
    for x in results:
        print(x)
    
   
def em_list():
    import mysql.connector as sql
    conn=sql.connect(host='localhost',user='root',password='12345',database='Payroll')
    mycursor=conn.cursor()
    mycursor.execute("select em_name from office order by em_name asc")
    list_=mycursor.fetchall()
    for x in list_:
        print (x)

        
def em_count():
    import mysql.connector as sql
    conn=sql.connect(host='localhost',user='root',password='12345',database='Payroll')
    mycursor=conn.cursor()
    mycursor.execute("select count(distinct em_name) from office")
    count=mycursor.fetchall()
    for x in count:
        print("    numbr of employees: ",x)
    conn.commit()


def em_salary():
    import mysql.connector as sql
    conn=sql.connect(host='localhost',user='root',password='12345',database='Payroll')
    mycursor=conn.cursor()
    nam=input("enter your name")
    mycursor.execute("update office set em_salary=em_salary+em_salary*10/100 where em_name='{}'".format(nam))
    conn.commit()

    
def salary():
    nam=input("enter your name :")
    a=mycursor.execute("select em_salary from office where em_name='{}'".format(nam))
    mycursor.execute(a)
    salary=mycursor.fetchall()
    for x in salary:
        print(        x,"is your current salary",nam       )
    conn.commit()

    
menu()  
