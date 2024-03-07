import mysql.connector as myConn

mydb = myConn.connect(host="localhost", user='root', password='admin', database='Learncoding')

db_cursor = mydb.cursor()

db_cursor.execute("""INSERT INTO emp(Roll, Ename) values(20, "Vishal")""")
mydb.commit()

print(db_cursor.rowcount, "record inserted")