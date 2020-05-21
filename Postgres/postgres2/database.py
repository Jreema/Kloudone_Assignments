import psycopg2
class DatabaseObject(object):
    def __init__(self):
        try:
            connection = psycopg2.connect(user = "user1",
                                  password = "******",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "mydb")
            with connection:
                cur =connection.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS employee (eid SMALLSERIAL PRIMARY KEY, ename VARCHAR(30) NOT NULL, dept VARCHAR(25), designation VARCHAR(25) NOT NULL, salary INTEGER);")
                connection.commit()


        except (Exception, psycopg2.Error) as error :
            print ("Unable to Create Table", error)

        finally:
            #closing database connection.
            if(connection):
                cur.close()
                connection.close()

    def insert_data(self,data):
        try:
            connection = psycopg2.connect(user="user1",
                                         password="*****",
                                         host="127.0.0.1",
                                         port="5432",
                                         database="mydb")
            cursor = connection.cursor()

            postgres_insert_query = """ INSERT INTO employee (ename,dept,designation,salary) VALUES (%s,%s,%s,%s)"""
            cursor.execute(postgres_insert_query,data)

            connection.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into employee table")

        except (Exception, psycopg2.Error) as error:
            if (connection):
                print("Failed to insert record into mobile table", error)

        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
    def view_data(self):
        try:
            connection = psycopg2.connect(user="user1",
                                         password="*****",
                                         host="127.0.0.1",
                                         port="5432",
                                         database="mydb")
            cursor = connection.cursor()

            postgres_select_query = """SELECT * FROM employee;"""
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

    def delete_data(self,id):
        try:
            connection = psycopg2.connect(user="user1",
                                          password="*****",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="mydb")
            cursor = connection.cursor()
            sql_delete_query = """Delete from employee where eid = %s"""
            cursor.execute(sql_delete_query, (id))
            connection.commit()
            count = cursor.rowcount
            print(count, "Record deleted successfully ")

        except (Exception, psycopg2.Error) as error:
            print("Error in Delete operation", error)

        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
            print("PostgreSQL connection is closed")


    def update_data(self,data):
        try:
            connection = psycopg2.connect(user="user1",
                                          password="******",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="mydb")
            cursor = connection.cursor()
            sql_update_query = """Update employee set salary = %s where eid = %s"""
            cursor.execute(sql_update_query, (data[0], data[1]))
            connection.commit()
            count = cursor.rowcount
            print(count, "Record Updated successfully ")
        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)

        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")


def main():
    print("*"*40)
    print("Employee Management System")
    print("*"*40)
    db = DatabaseObject()
    loop= True
    while(loop):
        choice = input("Press 1. Insert an Employee\t2. View all Employees\t3. Delete an Employee\t4. Update Employee\t5. Exit ")
        if choice=='1':
            name = input("Enter the Employee name: ")
            dept = input("Enter the department: ")
            designation = input("Enter the designation: ")
            salary = input("Enter the salary: ")
            db.insert_data((name,dept,designation,salary))

        elif choice== '2':
            for index, item in enumerate(db.view_data()):
                print("Id: "+ str(item[0]))
                print("Employee Name: "+ item[1])
                print("Department: "+ item[2])
                print("Designation: "+item[3])
                print("Salary: "+str(item[4]))
                print("\n")

        elif choice == '3':
            id = input("Enter the Employee Id to be deleted: ")
            db.delete_data((id))
        elif choice=='4':
            id =int(input("Enter the Employee Id to be updated: "))
            sal =int(input("Enter the Salary: "))
            db.update_data((sal,id))

        else:
            loop=False


if __name__ == '__main__':
    main()
