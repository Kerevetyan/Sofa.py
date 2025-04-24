import sqlite3

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS menu (

id INTEGER PRIMARY KEY AUTOINCREMENT,
dish TEXT,
category TEXT,
price INT,
available TEXT
)
''')
cursor.execute("INSERT INTO menu (dish, category, price, available) VALUES ('chiken', 'main_dish', 66, 'YES')")
cursor.execute("INSERT INTO menu (dish, category, price, available) VALUES ('reebs', 'main_dish', '85', 'YES')")
cursor.execute("INSERT INTO menu (dish, category, price, available) VALUES ('cake', 'desert', '25', 'YES')")
cursor.execute("INSERT INTO menu (dish, category, price, available) VALUES ('cheese_cake', 'desert', '30', 'NO')")
cursor.execute("INSERT INTO menu (dish, category, price, available) VALUES ('steak', 'main_dish', '30', 'NO')")
cursor.execute("INSERT INTO menu (dish, category, price, available) VALUES ('ice_cream', 'desert', '40', 'YES')")

cursor.execute("SELECT dish, category, price, available FROM menu WHERE dish LIKE '%reebs%'")
print(cursor.fetchall())
cursor.execute("SELECT dish, category, price, available FROM menu WHERE category LIKE '%desert%'")
print(cursor.fetchall())
cursor.execute("SELECT dish, category, price, available FROM menu WHERE price < 30 AND available LIKE '%YES%'")
print(cursor.fetchall())
cursor.execute("SELECT dish, category, price, available FROM menu WHERE price > 50 AND category LIKE '%main_dish%'")
print(cursor.fetchall())

conn.commit()
conn.close()



import sqlite3

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS music (

id INTEGER PRIMARY KEY AUTOINCREMENT,
song TEXT,
author TEXT,
year INT
)
''')
cursor.execute("INSERT INTO music (song, author, year) VALUES ('Born To Die', 'Lana Del Rey', 2012)")
cursor.execute("INSERT INTO music (song, author, year) VALUES ('heartbeat', 'childish gambino', 2012)")
cursor.execute("INSERT INTO music (song, author, year) VALUES ('Pretty', 'Coco & Clair Clair', 2021)")
cursor.execute("INSERT INTO music (song, author, year) VALUES ('Renegade', 'Aaryan Shah', 2022)")

cursor.execute("SELECT song, author, year FROM music WHERE song LIKE '%B%'")
print(cursor.fetchall())
cursor.execute("SELECT song, author, year FROM music WHERE author LIKE '%C%'")
print(cursor.fetchall())
cursor.execute("SELECT song, author, year FROM music WHERE year > 2013")
print(cursor.fetchall())

conn.commit()
conn.close()
