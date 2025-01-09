import sqlite3

# соеденение с базой данных  с помощью слова connect
with sqlite3.connect('./database.db') as db: # db db3 sqlite sqlite3  database.db - имя файла базы данных
                                            # . - текущая директория
    # создание таблицы в бд
    #cursor = db.cursor()
    #query = """ CREATE TABLE IF NOT EXISTS expenses(id INTEGER, name TEXT) """
    #cursor.execute(query)
    # заполнение таблицы в бд

    cursor = db.cursor()
    query = """ INSERT INTO expenses (id, name) VALUES(1, 'коммуналка') """
    query1 = """ INSERT INTO expenses (name, id) VALUES('бензин', 2) """
    query2 = """ INSERT INTO expenses VALUES(3, 'интернет') """
    cursor.execute(query)
    cursor.execute(query1)
    cursor.execute(query2)
    # перед закрытием обязательно нужно закомитить
    db.commit()



