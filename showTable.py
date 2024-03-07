import mysql.connector as myConn

mydb = myConn.connect(host="localhost", user='root', password='admin', database='Learncoding')

db_cursor = mydb.cursor()

db_cursor.execute("""SHOW TABLES""")

for table in db_cursor:
    print(table)

