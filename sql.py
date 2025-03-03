import sqlite3

conn = sqlite3.connect("my_db.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT UNIQUE           
    )            
''')

cursor.execute('''
    INSERT INTO users (username, email) VALUES ('john_psina', 'johnsuperpsina@mail.ru')


''')

conn.commit()

cursor.execute('''
    SELECT id, username, email FROM users
''')

rows = cursor.fetchall()

for row in rows:
    print(f'ID: {row[0]}, Username: {row[1]}, Email: {row[2]}')

conn.close()

