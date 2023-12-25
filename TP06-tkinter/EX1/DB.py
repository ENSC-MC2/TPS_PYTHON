import sqlite3 as db

class DB():
    def __init__(self):
        print("DB created")
        self.con = db.connect("mydatabase.db")
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY autoincrement, 
                        name TEXT, 
                        email TEXT,
                        age INTEGER);''')
        self.con.commit()
    
    def insert_data(self, name, email, age):
        self.cur.execute('''INSERT INTO students (name, email, age) VALUES (?, ?, ?);''', (name, email, age))
        self.con.commit()

    def get_data(self):
        self.cur.execute('''SELECT * FROM students;''')
        data = self.cur.fetchall()
        return data