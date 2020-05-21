from tkinter import *
import psycopg2

root =Tk()
root.title("Drop Down Box Demo")
root.geometry("400x400")

def fetch_records():
    try:
        connection = psycopg2.connect(user="reema1",
                                  password="mathi200",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="mydb")
        cursor = connection.cursor()

        postgres_select_query = """SELECT eid FROM employee;"""
        cursor.execute(postgres_select_query)
        return cursor.fetchall()

    except (Exception, psycopg2.Error) as error:
        if (connection):
            print("Failed to retrieve records from employee table", error)

    finally:
        # closing database connection.
        if (connection):
             cursor.close()
             connection.close()
             print("PostgreSQL connection is closed")


def fetch_row(event):
    data1 =clicked.get()
    print(data1[1])
    try:
        connection = psycopg2.connect(user="reema1",
                                  password="mathi200",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="mydb")
        cursor = connection.cursor()

        postgres_select_query = """SELECT * FROM employee where eid = %s;"""
        cursor.execute(postgres_select_query,data1[1])
        data=  cursor.fetchall()
        print(data)
        for index,item in enumerate(data):
            label1["text"] = "Employeee ID: "+ str(item[0])
            label2["text"]= "Employee Name: "+item[1]
            label3["text"]= "Department: " +item[2]
            label4["text"]= "Designation: "+item[3]
            label5["text"]="Salary: "+str(item[4])


    except (Exception, psycopg2.Error) as error:
        if (connection):
            print("Failed to retrieve records from employee table", error)

    finally:
        # closing database connection.
        if (connection):
             cursor.close()
             connection.close()
             print("PostgreSQL connection is closed")




options =fetch_records()

clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root,clicked,*options,command=fetch_row)
drop.pack(ipady =10)
label1 = Label(root,text="")
label1.pack()
label2 = Label(root,text="")
label2.pack()
label3 = Label(root,text="")
label3.pack()
label4 = Label(root,text="")
label4.pack()
label5 = Label(root,text="")
label5.pack()
root.mainloop()