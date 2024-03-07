import mysql.connector as myConn

mydb = myConn.connect(host="localhost", user='root', password='admin', database='Learncoding')
db_cursor = mydb.cursor()

db_query = """INSERT INTO emp(Roll, Ename) values(%s, %s)"""
record_list = [(30, "Vishal"), (40, "Kumar"), (50,"Rohit")]

db_cursor.executemany(db_query, record_list)
mydb.commit()

print(db_cursor.rowcount, "record inserted")