import sqlite3 as db

# Connect to database
conn = db.connect('school.db')

curs = conn.cursor()

# 1: Create table
curs.execute('''CREATE TABLE IF NOT EXISTS students (
    id integer primary key autoincrement,
    name text,
    email text,
    phone integer,
    section text     
)''')

conn.commit()

# 2 : insert

data ={
    'name' : 'ahmed',
    'email' : 'ahmed@gmail.com',
    'phone' : 666589435,
    'section' : 'math' 
}

curs.execute('''INSERT INTO students (name, email, phone, section) VALUES (:name, :email, :phone, :section)''', data)

conn.commit()

# 3 : insert from user input
name = input("Saisir le nom de l'étudiant : ")
email = input("Saisir l'email de l'étudiant : ")
phone = int(input("Saisir le téléphone de l'étudiant : "))
section = input("Saisir la section de l'étudiant : ")

curs.execute('''INSERT INTO students (name, email, phone, section) VALUES (?, ?, ?, ?)''', (name, email, phone, section))
conn.commit()

# 4 : select
print("Liste des étudiants : ")

print("ID\tName\tEmail\t\tPhone\t\tSection")
for row in curs.execute('''SELECT * FROM students''') :
    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")

# 5: delete ahmed 
curs.execute('''DELETE FROM students WHERE name = ?''', ('ahmed',))
conn.commit()
conn.close()