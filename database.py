import mysql.connector as myConn
mydb = myConn.connect(host="localhost", user = "root", password = "admin")

db_cursor = mydb.cursor() # help to execute the sql query

db_cursor.execute("""CREATE DATABASE LearnCoding""")
