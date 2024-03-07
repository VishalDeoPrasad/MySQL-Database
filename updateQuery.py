import mysql.connector as myConn

my_db = myConn.connect(host="localhost", user='root', password='admin', database='Learncoding')
db_cursor = my_db.cursor()

db_query = """UPDATE Learncoding.emp SET Ename=%s WHERE Ename=%s"""
db_value = ("Chikku", "Vishal")
db_cursor.execute(db_query, db_value)

my_db.commit()
print(db_cursor.rowcount, "data updated")