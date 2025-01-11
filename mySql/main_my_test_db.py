import mysql.connector
# crete database my_test_db

SECRET_KEY = 'some_key'
db = mysql.connector.connect(host="localhost", 
                               database="my_test_db", user="root", 
                               password=SECRET_KEY)


cursor = db.cursor()


query = """SELECT * FROM worckers JOIN professions WHERE worckers.profession = professions.profession;"""
cursor.execute(query)

for row in cursor:
    print(row)