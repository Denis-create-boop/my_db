import mysql.connector
import sys
sys.path.append('C:\\Users\\Den_1\\Desktop\\packeges')

from main import SECRET_KEY


class Professions:


    def get_id(self):
        db = mysql.connector.connect(host='localhost', 
                                     database='my_test_db',
                                     user='root',
                                     password=SECRET_KEY)
        cursor = db.cursor()
        query = """SELECT MAX(id) FROM professions;"""
        cursor.execute(query)
        for row in cursor:
            count = row[0]
        return count


    def add_profession(self, profession, floor):
        db = mysql.connector.connect(host='localhost', 
                                     database='my_test_db',
                                     user='root',
                                     password=SECRET_KEY)
        cursor = db.cursor()
        count = self.get_id()
        query = """INSERT INTO professions(id, profession, floor) VALUES(%s, %s, %s);"""

        if count is None:
            ls_insert = (1, profession, floor)
        else:
            ls_insert = (count + 1, profession, floor)
        cursor.execute(query, ls_insert)
        db.commit()

    def del_profession(self, profession):
        db = mysql.connector.connect(host='localhost', 
                                     database='my_test_db',
                                     user='root',
                                     password=SECRET_KEY)
        cursor = db.cursor()
        query = """DELETE FROM professions WHERE profession = %s;"""
        cursor.execute(query, (profession,))
        db.commit()

        
a = Professions()
#a.add_profession('programmer', 6)
#a.del_profession('programmer')

db = mysql.connector.connect(host='localhost', 
                                database='my_test_db',
                                user='root',
                                password=SECRET_KEY)
cursor = db.cursor()
query = """SELECT * FROM professions;"""
cursor.execute(query)

for row in cursor:
    print(row)