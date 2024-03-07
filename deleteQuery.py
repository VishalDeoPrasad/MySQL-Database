import mysql.connector as myConn

my_db = myConn.connect(host="localhost", user="root", password="admin", database="Learncoding")
db_cursor = my_db.cursor()

my_query = """ DELETE FROM Learncoding.emp WHERE Ename=%s """
my_value = ("Rohit", )

db_cursor.execute(my_query, my_value)
my_db.commit()

print(db_cursor.rowcount, "Record Deleted!!!")
