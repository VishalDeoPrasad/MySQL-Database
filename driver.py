import mysql.connector as myConn
mydb = myConn.connect(host="localhost",
                    user = "root",
                    password = "admin")
print(mydb, "Connection Establisted...")