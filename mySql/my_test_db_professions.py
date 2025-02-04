import mysql.connector
import sys

sys.path.append("C:\\Users\\Den_1\\Desktop\\packeges")

from main import SECRET_KEY


db = mysql.connector.connect(
    host="localhost", database="my_test_db", user="root", password=SECRET_KEY
)
# crete database my_test_db


class Professions:

    def __init__(self):
        self.cursor = db.cursor()

    # создать таблицу
    def create(self):
        query = """CREATE TABLE IF NOT EXISTS professions 
        (id INTEGER, profession VARCHAR(50), amount VARCHAR(50))"""
        self.cursor.execute(query)
        db.commit()

    # получить последний id
    def get_id(self):
        self.create()
        query = """SELECT MAX(id) FROM professions"""
        self.cursor.execute(query)
        for row in self.cursor:
            if row[0] is None:
                return 1
            else:
                return int(row[0]) + 1

    def all_id(self):
        query = """SELECT id FROM professions"""
        self.cursor.execute(query)
        return self.cursor
    
    # получаем количество сотрудников
    def get_amount(self, prof):
        self.create()
        query = """SELECT amount FROM professions WHERE profession = %s"""
        self.cursor.execute(query, (prof,))
        for row in self.cursor:
            return row

    def change_amount(self, amount, prof):
        self.create()
        query = """UPDATE professions SET amount=%s WHERE profession=%s"""
        self.cursor.execute(query, (amount, prof,))
        db.commit()

    # смотрим все что есть в таблице
    def show_all(self):
        self.create()
        query = """SELECT * FROM professions"""
        self.cursor.execute(query)
        return self.cursor

    # смотрим все профессии
    def show_profession(self):
        self.create()
        query = """SELECT profession FROM professions"""
        ls_prof = []
        self.cursor.execute(query)
        for row in self.cursor:
            ls_prof.append(row[0])
        return ls_prof

    # записываем новую профессиию
    def write(self, prof, am=None):
        self.create()
        id = self.get_id()
        if not am:
            amount = self.get_amount(prof)
            if amount is None:
                amount = 0
            else:
                amount = int(amount[0]) + 1
        else:
            amount = am
        ls_prof = self.show_profession()

        if prof not in ls_prof or ls_prof is None:
            query = """INSERT INTO professions (id, profession, amount) VALUES(%s, %s, %s)"""
            ls = (
                id,
                prof,
                amount,
            )
            self.cursor.execute(query, ls)
            db.commit()

    # получаем все id
    def show_profession_id(self):
        self.create()
        ls_id = []
        query = """SELECT id FROM professions"""
        self.cursor.execute(query)
        for row in self.cursor:
            ls_id.append(int(row[0]))
        return ls_id

    # изменяем название професии
    def change_name(self, id, prof):
        self.create()
        if id in self.show_profession_id():
            query = """UPDATE professions SET profession = %s WHERE id = %s"""
            self.cursor.execute(
                query,
                (
                    prof,
                    id,
                ),
            )
            db.commit()
            return f"Название успешно изменено"
        else:
            return f"Введен неверный id"

    # удаляем профессиию
    def del_prof(self, prof):
        self.create()
        if prof in self.show_profession():
            amount = self.get_amount(prof)[0]
            if int(amount[0]) == 0:
                query = """DELETE FROM professions WHERE profession = %s"""
                self.cursor.execute(query, (prof,))
                db.commit()
                return f"Провессия '{prof}' успешно удалена из базы данных"
            else:
                return f"Ошибка. За профессией '{prof}' числиться {int(amount)} человек, пожалуйста сначала удалите персонал"
        else:
            return f"Профессии '{prof}' нет в базы данных"
