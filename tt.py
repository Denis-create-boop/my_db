import mysql.connector

conn = mysql.connector.connect(host="localhost", 
                               database="temp", user="root", 
                               password="LiZa04031994")


cursor = conn.cursor()
query = """ SELECT * FROM person """

cursor.execute(query)

for row in cursor:
    print(row)

