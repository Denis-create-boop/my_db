from my_test_db_professions import db

# crete database my_test_db


class Worckers:
    def __init__(self):
        self.cursor = db.cursor()

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

    # добавляем сотрудников
    def write_worcker(
        self,
        name=None,
        first_name=None,
        address=None,
        phone=None,
        profession=None,
        status=None,
    ):
        self.create_table()
        query = """INSERT INTO worckers (id, name, first_name, address, phone, profession, status) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        ls_write = (1, name, first_name, address, phone, profession, status)
        self.cursor.execute(query, ls_write)
        db.commit()

    # show all worcker
    def show_worckers(self):
        query = """SELECT * FROM worckers"""
        self.cursor.execute(query)
        return self.cursor

    # change worcker's profession
    def change_worcker_profession(
        self, id=None, name=None, first_name=None, profession=None
    ):
        if id:
            query = """UPDATE worckers SET profession = %s WHERE id=%s"""
            self.cursor.execute(
                query,
                (
                    profession,
                    id,
                ),
            )
        elif name and first_name:
            query = (
                """UPDATE worckers SET profession=%s WHERE name=%s AND first_name=%s"""
            )
            self.cursor.execute(
                query,
                (
                    profession,
                    name,
                    first_name,
                ),
            )
        db.commit()

    def change_worcker_name(self, id=None, name=None, first_name=None, new_name=None):
        if id:
            query = """UPDATE worckers SET name=%s WHERE id=%s"""
            self.cursor.execute(
                query,
                (
                    new_name,
                    id,
                ),
            )

        elif name and first_name:
            query = """UPDATE worckers SET name=%s WHERE name=%s AND first_name=%s"""
            self.cursor.execute(
                query,
                (
                    new_name,
                    name,
                    first_name,
                ),
            )

        db.commit()

    def change_worcker_first_name(
        self, id=None, name=None, first_name=None, new_first_name=None
    ):
        if id:
            query = """UPDATE worckers SET first_name=%s WHERE id=%s"""
            self.cursor.execute(
                query,
                (
                    new_first_name,
                    id,
                ),
            )

        elif name and first_name:
            query = (
                """UPDATE worckers SET first_name=%s WHERE name=%s AND first_name=%s"""
            )
            self.cursor.execute(
                query,
                (
                    new_first_name,
                    name,
                    first_name,
                ),
            )

        db.commit()

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


p = Worckers()
# p.change_worcker_profession(name='Petya', first_name='Vass', profession='develop')
# p.change_worcker_name(name='Denis', first_name='Vass', new_name='Petya')


d = p.show_worckers()
for row in d:
    print(row)
