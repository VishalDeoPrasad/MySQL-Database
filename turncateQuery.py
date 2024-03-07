import mysql.connector as myConn

my_db = myConn.connect(host="localhost", user="root", password="admin", database="Learncoding")
db_cursor = my_db.cursor()

my_query = """ TRUNCATE TABLE Learncoding.emp """

db_cursor.execute(my_query)
my_db.commit()

print("All Record Deleted!!!")
