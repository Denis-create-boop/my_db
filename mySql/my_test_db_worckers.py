from my_test_db_professions import db

# crete database my_test_db


class Worckers:
    def __init__(self, id=None, name=None, first_name=None):
        self.cursor = db.cursor()
        self.id = id
        self.name = name
        self.first_name = first_name

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
        query = """SELECT MAX(id) FROM worckers"""
        self.cursor.execute(query)
        for row in self.cursor:
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

    # show all worcker
    def show_worckers(self):
        query = """SELECT name, first_name FROM worckers"""
        self.cursor.execute(query)
        return self.cursor


    def show_all(self):
        query = """SELECT * FROM worckers"""
        self.cursor.execute(query)
        return self.cursor


    def get_prof(self):
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
        

    # change worcker's profession
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

    # change name
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

    #change first_name
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

    #change address
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

    # delete address
    def del_worcker_address(self):
        if self.id:
            query = """UPDATE worckers SET address=None WHERE id=%s"""
            self.cursor.execute(query, (self.id,))
        elif self.name and self.first_name:
            query = """UPDATE worckers SET address=None WHERE name=%s AND first_name=%s"""
            self.cursor.execute(query, (str(self.name).capitalize(), str(self.first_name).capitalize(),))
        db.commit()

    # change phone
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

    # delete phone
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

    #change status
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

    # delete worcker
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
