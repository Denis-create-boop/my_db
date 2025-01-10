import mysql.connector
# crete database my_test_db

SECRET_KEY = 'LiZa04031994'
db = mysql.connector.connect(host="localhost", 
                               database="my_test_db", user="root", 
                               password=SECRET_KEY)


cursor = db.cursor()

# создал таблицу worckers
#query = """CREATE TABLE worckers(
#            id INTEGER,
#            name VARCHAR(50),
#            first_name VARCHAR(50),
#            address VARCHAR(50),
#            phone VARCHAR(11)
#            );
#        """


# добавил работника
#query = """INSERT INTO worckers VALUES (1, 'Denis', 'Popov', 'lenina 45', '89203415725')"""

# добавил второго
#query = """INSERT INTO worckers VALUES (2, 'Vasay', 'Sidorov', 'kuchigina 43', '89501324782')"""



#query = """SELECT * FROM worckers;"""
cursor.execute(query)
db.commit()



for row in cursor:
    print(row)




