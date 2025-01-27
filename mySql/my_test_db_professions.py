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


    def create(self):
        query = """CREATE TABLE IF NOT EXISTS professions 
        (id INTEGER, profession VARCHAR(50), amount VARCHAR(50))"""
        self.cursor.execute(query)
        db.commit()

    
    def get_id(self):
        query = """SELECT MAX(id) FROM professions"""
        self.cursor.execute(query)
        for row in self.cursor:
            if row[0] is None:
                return 1
            else:
                return int(row[0]) + 1
        

    def get_amount(self, prof):
        query = """SELECT amount FROM professions WHERE profession = %s"""
        self.cursor.execute(query, (prof, ))
        for row in self.cursor:
            return row


    def show_all(self):
        query = """SELECT * FROM professions"""
        self.cursor.execute(query)
        return self.cursor


    def show_profession(self):
        query = """SELECT profession FROM professions"""
        ls_prof = []
        cursor.execute(query)
        for row in cursor:
            ls_prof.append(row[0])
        return ls_prof
    

    def write(self, prof):
        self.create()
        id = self.get_id()
        amount = self.get_amount(prof)
        if amount is None:
            amount = 0
        else:
            amount = int(amount[0]) + 1
        ls_prof = self.show_profession()
        
        if prof not in ls_prof or ls_prof is None:
            query = """INSERT INTO professions (id, profession, amount) VALUES(%s, %s, %s)"""
            ls = (id, prof, amount,)
            self.cursor.execute(query, ls)
            db.commit()

            
