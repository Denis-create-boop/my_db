import mysql.connector
from main_my_test_db import SECRET_KEY
# crete database my_test_db


db = mysql.connector.connect(host="localhost", 
                               database="my_test_db", 
                               user="root", 
                               password=SECRET_KEY)


cursor = db.cursor()


# создал таблицу professions с полями id - порядковый номер, profession - название провессии, 
# floor - номер этажа на котором находиться этот отдел
query = """CREATE TABLE professions(
            id INTEGER,
            profession VARCHAR(50),
            floor INTEGER);      
        """

cursor.execute(query)
db.commit()


# добавил профессии в таблицу
query = """INSERT INTO professions (id, profession, floor)
                VALUES (1, 'backend developer', 2),
                (2, 'frontend developer', 3),
                (3, 'QA manager', 4),
                (4, 'software tester', 4);
        """



cursor.execute(query)
db.commit()


