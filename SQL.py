import sqlite3
conn = sqlite3.connect('my_database3.db')
cursor = conn.cursor()

# Створення таблиці (якщо її ще немає)
cursor.execute('''
CREATE TABLE IF NOT EXISTS library (

id INTEGER PRIMARY KEY AUTOINCREMENT,
author TEXT,
song TEXT,
game TEXT,
comics TEXT,
year INTEGER
)
''')

cursor.execute("INSERT INTO library (song, author, year) VALUES ('heartbeat', 'childish gambino', 2012)")
cursor.execute("INSERT INTO library (game, author, year) VALUES ('S. T. A. L. K. E. R. 2', 'Yaroslav Kravchenko', 2024)")
cursor.execute("INSERT INTO library (comics, author, year) VALUES ('Jujutsu Kaisen', 'Gege Akutami', 2018)")

cursor.execute("SELECT * FROM library")
print(cursor.fetchall()) # Вивести всі записи з таблиці

# Закриття з'єднання
conn.close() 
