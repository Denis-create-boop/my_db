from my_test_db_professions import db
# crete database my_test_db


class Worckers:
    def __init__(self):
        self.cursor = db.cursor()

    def create(self):
        # создал таблицу worckers
        query = """CREATE TABLE IF NOT EXISTS worckers(
            id INTEGER,
            name VARCHAR(50),
            first_name VARCHAR(50),
            address VARCHAR(50),
            phone VARCHAR(11),
            profession VARCHAR(50)
            );
        """
        self.cursor.execute(query)
        db.commit()


    def write(self, name, first_name, address, phone, profession):
        self.create()
        query = """INSERT INTO worckers (id, name, first_name, address, phone, profession) 
        VALUES (%s, %s, %s, %s, %s, %s)"""
        ls_write = (name, first_name, address, phone, profession)
        self.cursor.execute(query, ls_write)
        db.commit()

