import sqlite3

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# Створення таблиці
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
''')

# Меню
print("Привіт! Це програма, яка керує базою користувачів.")
print("1 - Змінити інформацію про користувача")
print("2 - Видалити користувача")
print("Інше - Додати нового користувача")

user_input = input("Вибери опцію: ")

if user_input == "1":
    user_id = input("Введи ID користувача, якого хочеш змінити: ")
    new_name = input("Нове ім'я: ")
    new_age = input("Новий вік: ")
    cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (new_name, new_age, user_id))
    conn.commit()
    print("Користувача оновлено!")

elif user_input == "2":
    user_id = input("Введи ID користувача, якого хочеш видалити: ")
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    print("Користувача видалено!")

else:
    name = input("Введи ім'я нового користувача: ")
    age = input("Введи вік: ")
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print("Користувача додано!")

# Показати всіх користувачів
print("\nУсі користувачі в базі:")
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

conn.close()


import sqlite3
import tkinter as tk
from tkinter import messagebox

# Підключення до бази
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
''')
conn.commit()

# Функції
def add_user():
    name = name_entry.get()
    age = age_entry.get()
    if name and age:
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
        messagebox.showinfo("Успіх", "Користувача додано!")
        refresh_users()
    else:
        messagebox.showwarning("Помилка", "Введіть ім'я та вік!")

def update_user():
    try:
        user_id = int(id_entry.get())
        new_name = name_entry.get()
        new_age = age_entry.get()
        cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (new_name, new_age, user_id))
        conn.commit()
        messagebox.showinfo("Успіх", "Інформацію оновлено!")
        refresh_users()
    except:
        messagebox.showerror("Помилка", "Перевірте правильність ID!")

def delete_user():
    try:
        user_id = int(id_entry.get())
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        messagebox.showinfo("Успіх", "Користувача видалено!")
        refresh_users()
    except:
        messagebox.showerror("Помилка", "Введіть правильний ID!")

def refresh_users():
    users_list.delete(0, tk.END)
    cursor.execute("SELECT * FROM users")
    for user in cursor.fetchall():
        users_list.insert(tk.END, f"ID {user[0]}: {user[1]}, {user[2]} років")

# Вікно
root = tk.Tk()
root.title("Менеджер користувачів")

# Ввід
tk.Label(root, text="ID (для змін/видалення):").grid(row=0, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)

tk.Label(root, text="Ім'я:").grid(row=1, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1)

tk.Label(root, text="Вік:").grid(row=2, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1)

# Кнопки
tk.Button(root, text="Додати користувача", command=add_user).grid(row=3, column=0, pady=5)
tk.Button(root, text="Оновити користувача", command=update_user).grid(row=3, column=1, pady=5)
tk.Button(root, text="Видалити користувача", command=delete_user).grid(row=4, column=0, columnspan=2)

# Список користувачів
users_list = tk.Listbox(root, width=150, height=80)
users_list.grid(row=5, column=0, columnspan=2, pady=10)

refresh_users()

root.mainloop()
conn.close()
