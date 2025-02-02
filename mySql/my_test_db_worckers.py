from my_test_db_professions import db
# crete database my_test_db


class Worckers:
    def __init__(self):
        self.cursor = db.cursor()

    def create_table(self):
        # создал таблицу worckers
        query = """CREATE TABLE IF NOT EXISTS worckers(
            id INTEGER,
            name VARCHAR(50),
            first_name VARCHAR(50),
            address VARCHAR(50),
            phone VARCHAR(11),
            profession VARCHAR(50),
            status VARCHAR(50)
            );
        """
        self.cursor.execute(query)
        db.commit()

    # добавляем сотрудников
    def write_worcker(self, name, first_name, address, phone, profession, status):
        self.create_table()
        query = """INSERT INTO worckers (id, name, first_name, address, phone, profession, status) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        ls_write = (name, first_name, address, phone, profession, status)
        self.cursor.execute(query, ls_write)
        db.commit()


    def change_worcker_profession(self):
        pass


    def change_worcker_name(self):
        pass


    def change_worcker_first_name(self):
        pass


    def change_worcker_address(self):
        pass


    def add_worcker_address(self):
        pass


    def del_worcker_address(self):
        pass


    def change_worcker_phone(self):
        pass


    def add_worcker_phone(self):
        pass


    def del_worcker_phone(self):
        pass

    
    def change_worcker_status(self):
        pass

    
    def del_worcker(self):
        pass

