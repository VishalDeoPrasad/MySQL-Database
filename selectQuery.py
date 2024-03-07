import mysql.connector as myConn

mydb = myConn.connect(host="localhost", user='root', password='admin', database='Learncoding')
db_cursor = mydb.cursor()

db_query = """SELECT * FROM Learncoding.emp"""
db_cursor.execute(db_query)

for row in db_cursor.fetchall():
    print(row)