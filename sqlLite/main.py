import sqlite3
import datetime

# соеденение с базой данных  с помощью слова connect
#with sqlite3.connect('./database.db') as db: # db db3 sqlite sqlite3  database.db - имя файла базы данных
#                                            # . - текущая директория
#     #создание таблицы в бд
#    cursor = db.cursor()
#    query = """ CREATE TABLE IF NOT EXISTS expenses(id INTEGER, name TEXT) """
#    cursor.execute(query)
#     #заполнение таблицы в бд
#
#    cursor = db.cursor()
#    query = """ INSERT INTO expenses (id, name) VALUES(1, 'коммуналка') """
#    query1 = """ INSERT INTO expenses (name, id) VALUES('бензин', 2) """
#    query2 = """ INSERT INTO expenses VALUES(3, 'интернет') """
#    cursor.execute(query)
#    cursor.execute(query1)
#    cursor.execute(query2)
#    # перед закрытием обязательно нужно закомитить
#    db.commit()


def get_timestamp(y, m, d):
    return datetime.datetime.timestamp(datetime.datetime(y, m, d))


def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()


#insert_payments = [
#    (1, 120, get_timestamp(2020, 9, 1), 1),
#    (2, 12, get_timestamp(2020, 9, 1), 3),
#    (3, 20, get_timestamp(2020, 9, 1), 2),
#    (4,120, get_timestamp(2020, 9, 2), 2),
#    (5, 20, get_timestamp(2020, 9, 3), 2),
#    (6, 20, get_timestamp(2020, 9, 4), 2),
#    (7, 20, get_timestamp(2020, 9, 5), 2),
#]
#
#with sqlite3.connect('./database.db') as db:
#    cursor = db.cursor()
#    query = """ INSERT INTO payments(id, amount, payment_date, expense_id) 
#        VALUES(?, ?, ?, ?); """
#
#    cursor.executemany(query, insert_payments)
#    db.commit()
#    print(cursor.rowcount, 'OK')



with sqlite3.connect('./database.db') as db:
    cursor = db.cursor()
    query = """ SELECT amount, payment_date, name FROM payments JOIN expenses 
                ON expenses.id = payments.expense_id WHERE expense_id = 2 """

    cursor.execute(query)
    sum = 0
    for res in cursor:
        sum += res[0]
        print(res[0], get_date(res[1]), res[2])
    print('TOTAL', sum)
    