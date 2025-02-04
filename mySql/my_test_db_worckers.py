# импортируем базу данных которая подключена в файле профессий
from my_test_db_professions import db

# crete database my_test_db

# создаём класс для таблицы работников
class Worckers:
    def __init__(self, id=None, name=None, first_name=None):
        self.cursor = db.cursor()
        self.id = id
        self.name = name
        self.first_name = first_name
        # self.flag = False

    # создал таблицу worckers
    def create_table(self):
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
        # берем последний id из таблицы
        query = """SELECT MAX(id) FROM worckers"""
        self.cursor.execute(query)
        for row in self.cursor:
            # возвращаем последний id
            return row[0]

    # добавляем сотрудников
    def add_worcker(self, address=None, phone=None, profession=None, status=None,):
        id = self.create_table()
        if id is None:
            id = 1
        else:
            id += 1

        query = """INSERT INTO worckers (id, name, first_name, address, phone, profession, status) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        ls_write = (id, self.name, self.first_name, address, phone, profession, status)
        self.cursor.execute(query, ls_write)
        db.commit()

    # функция для просмотра всех работников
    def show_worckers(self):
        self.create_table()
        query = """SELECT name, first_name FROM worckers"""
        self.cursor.execute(query)
        return self.cursor

    # функция для получения id всех работников
    def get_id(self):
        query = """SELECT id FROM worckers"""
        self.cursor.execute(query)
        return self.cursor

    # функция для просмотра всех полей таблицы
    def show_all(self):
        self.create_table()
        query = """SELECT * FROM worckers"""
        self.cursor.execute(query)
        return self.cursor

    # функция для получения профессии конкретного работника
    def get_prof(self):
        # если таблицы нет в бд то создаем
        self.create_table()
        if self.id:
            query = """SELECT profession FROM worckers WHERE id=%s"""
            self.cursor.execute(query, (self.id, ))
            for row in self.cursor:
                return row
        elif self.name and self.first_name:
            query = """SELECT profession FROM worckers WHERE name=%s AND first_name=%s"""
            self.cursor.execute(query, (self.name, self.first_name))
            for row in self.cursor:
                return row[0]

    # функция для изменения профессии работника
    def change_worcker_profession(
        self, profession=None
    ):
        if self.id:
            query = """UPDATE worckers SET profession = %s WHERE id=%s"""
            self.cursor.execute(
                query,
                (
                    profession,
                    self.id,
                ),
            )
        elif self.name and self.first_name:
            query = (
                """UPDATE worckers SET profession=%s WHERE name=%s AND first_name=%s"""
            )
            self.cursor.execute(
                query,
                (
                    profession,
                    str(self.name).capitalize(),
                    str(self.first_name).capitalize(),
                ),
            )
        db.commit()

    # функция для изменения имени работника
    def change_worcker_name(self, new_name=None):
        if self.id:
            query = """UPDATE worckers SET name=%s WHERE id=%s"""
            self.cursor.execute(
                query,
                (
                    str(new_name).capitalize(),
                    self.id,
                ),
            )
        elif self.name and self.first_name:
            query = """UPDATE worckers SET name=%s WHERE name=%s AND first_name=%s"""
            self.cursor.execute(
                query,
                (
                    str(new_name).capitalize(),
                    str(self.name).capitalize(),
                    str(self.first_name).capitalize(),
                ),
            )
        db.commit()

    # функция для изменения фамилии работника
    def change_worcker_first_name(
        self, new_first_name=None
    ):
        if self.id:
            query = """UPDATE worckers SET first_name=%s WHERE id=%s"""
            self.cursor.execute(
                query,
                (
                    str(new_first_name).capitalize(),
                    self.id,
                ),
            )
        elif self.name and self.first_name:
            query = (
                """UPDATE worckers SET first_name=%s WHERE name=%s AND first_name=%s"""
            )
            self.cursor.execute(
                query,
                (
                    str(new_first_name).capitalize(),
                    str(self.name).capitalize(),
                    str(self.first_name).capitalize(),
                ),
            )
        db.commit()

    # функция для изменения адреса работника
    def change_worcker_address(self, new_address=None):
        if self.id:
            query = """UPDATE worckers SET address=%s WHERE id=%s"""
            self.cursor.execute(query, (new_address, self.id,))
        elif self.name and self.first_name:
            query = """UPDATE worckers SET address=%s WHERE name=%s AND first_name=%s"""
            self.cursor.execute(
                query, 
                (
                    new_address, 
                    str(self.name).capitalize(), 
                    str(self.first_name).capitalize()
                )
            )
        db.commit()

    # функция для удаления адреса работника
    def del_worcker_address(self):
        if self.id:
            query = """UPDATE worckers SET address=None WHERE id=%s"""
            self.cursor.execute(query, (self.id,))
        elif self.name and self.first_name:
            query = """UPDATE worckers SET address=None WHERE name=%s AND first_name=%s"""
            self.cursor.execute(query, (str(self.name).capitalize(), str(self.first_name).capitalize(),))
        db.commit()

    # функция для изменения телефона работника
    def change_worcker_phone(self, phone):
        if self.id:
            query = """UPDATE worckers SET phone=%s WHERE id=%s"""
            self.cursor.execute(query, (phone, self.id,))
        elif self.name and self.first_name:
            query = (
                """UPDATE worckers SET phone=%s WHERE name=%s AND first_name=%s"""
            )
            self.cursor.execute(
                query,
                (
                    phone,
                    str(self.name).capitalize(),
                    str(self.first_name).capitalize(),
                ),
            )
        db.commit()

    # функция для удаления телефона работника
    def del_worcker_phone(self):
        if self.id:
            query = """UPDATE worckers SET phone=None WHERE id=%s"""
            self.cursor.execute(query, (self.id,))
        elif self.name and self.first_name:
            query = (
                """UPDATE worckers SET phone=None WHERE name=%s AND first_name=%s"""
            )
            self.cursor.execute(
                query,
                (
                    str(self.name).capitalize(),
                    str(self.first_name).capitalize(),
                ),
            )
        db.commit()

    # функция для изменения статуса работника
    def change_worcker_status(self, status):
        if self.id:
            query = """UPDATE worckers SET status=%s WHERE id=%s"""
            self.cursor.execute(
                query,
                (
                    status,
                    self.id,
                ),
            )
        elif self.name and self.first_name:
            query = """UPDATE worckers SET status=%s WHERE name=%s AND first_name=%s"""
            self.cursor.execute(
                query,
                (
                    str(status).lower(),
                    str(self.name).capitalize(),
                    str(self.first_name).capitalize(),
                ),
            )
        db.commit()

    # функция для удаления работника из бд
    def del_worcker(self):
        if self.id:
            query = """DELETE FROM worckers WHERE id=%s"""
            self.cursor.execute(query, (self.id,))
        elif self.name and self.first_name:
            query = (
                """DELETE FROM worckers WHERE name=%s AND first_name=%s"""
            )
            self.cursor.execute(
                query,
                (
                    self.name,
                    self.first_name,
                ),
            )
        db.commit()
