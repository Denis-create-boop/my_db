import mysql.connector
# crete database my_test_db

SECRET_KEY = 'LiZa04031994'
db = mysql.connector.connect(host="localhost", 
                               database="my_test_db", user="root", 
                               password=SECRET_KEY)


cursor = db.cursor()

# создал таблицу worckers
query = """CREATE TABLE worckers(
            id INTEGER,
            name VARCHAR(50),
            first_name VARCHAR(50),
            address VARCHAR(50),
            phone VARCHAR(11)
            );
        """

cursor.execute(query)
db.commit()


# добавил работника
query = """INSERT INTO worckers VALUES (1, 'Denis', 'Popov', 'lenina 45', '89203415725')"""

cursor.execute(query)
db.commit()

# добавил второго
query = """INSERT INTO worckers VALUES (2, 'Vasay', 'Sidorov', 'kuchigina 43', '89501324782')"""

cursor.execute(query)
db.commit()

# добавил столбец profession
query = """ALTER TABLE worckers ADD COLUMN profession VARCHAR(50);"""

cursor.execute(query)
db.commit()

# установил специальность для первого работника
query = """UPDATE worckers  SET 
           profession = 'backend developer' 
           WHERE id = 1;"""

cursor.execute(query)
db.commit()

# добавил специальность для второго работника
query = """UPDATE worckers SET 
            profession = 'frontent developer' 
            WHERE id = 2;"""

cursor.execute(query)
db.commit()

query = """SELECT * FROM worckers;"""
cursor.execute(query)




for row in cursor:
    print(row)
