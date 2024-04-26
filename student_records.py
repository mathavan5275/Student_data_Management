from tabulate import tabulate
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="Mathavan.0203",database="python")

def insert(Sname,Grade,Native):
    res=con.cursor()
    sql="insert into students(Sname,Grade,Native) values (%s,%s,%s)"
    user=(Sname,Grade,Native)
    res.execute(sql,user)
    con.commit()
    print("Data Inserted Succecfull ! ! !")
def update(Sname,Grade,Native,ID):
    res = con.cursor()
    sql = "update students set Sname=%s,Grade=%s,Native=%s where ID=%s"
    user = (Sname, Grade, Native,ID)
    res.execute(sql, user)
    con.commit()
    print("Data Updated Succecfull ! ! !")
def select():
    print("Here the Datas! ! !")
    res = con.cursor()
    sql="select ID,Sname,Grade,Native from students"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["ID","Sname","Grade","Native"]))
def delete(ID):
    res = con.cursor()
    sql = "delete from students where ID=%s"
    user = (ID,)
    res.execute(sql, user)
    con.commit()
    print("Data Deleted Succecfull ! ! !")

while True:
    print("1.Insert the Data")
    print("2.Update the Data")
    print("3.Select the Data")
    print("4.Delete the Data")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        # ID=input("Enter ID:")
        Sname=input("Enter Name:")
        Grade=input("Enter Grade:")
        Native=input("Enter Native:")
        insert(Sname, Grade,Native)
    elif choice==2:
        ID=input("Enter ID:")
        Sname=input("Enter Name:")
        Grade=input("Enter Grade:")
        Native=input("Enter Native:")
        update(Sname,Grade,Native,ID)
    elif choice==3:
        select()
    elif choice==4:
        ID=input("Enter ID to delete:")
        delete(ID)
    elif choice==5:
        quit()
    else:
        print("Invalid selection ! Try Again")



