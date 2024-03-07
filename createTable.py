import mysql.connector as myConn

mydb = myConn.connect(host="localhost", user='root', password='admin', database='Learncoding')

db_cursor = mydb.cursor()

db_cursor.execute("""CREATE TABLE Emp(
                  Roll int,
                  Ename varchar(20))""")

print("Table Created!!")