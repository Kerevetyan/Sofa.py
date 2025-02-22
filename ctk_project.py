import customtkinter as ctk
import random
from tkinter import messagebox

# Налаштування головного вікна
ctk.set_appearance_mode("black")
root = ctk.CTk()
root.title("Гра з випадковими кнопками")
root.geometry("900x700")
root.configure(fg_color="#9c76e8")

# Функція для появи кнопки у випадковому місці
def show_random_button():
    x, y = random.randint(80, 650), random.randint(80, 650)
    btn.place(x=x, y=y)

# Функція для початку гри
def start_game():
    messagebox.showinfo("Старт", "Гру почато!\nНатисніть Esc щоб завершити")
    start_btn.place_forget()
    show_random_button()

# Функція для завершення гри
def exit_game(event=None):
    root.destroy()

# Кнопка старту
start_btn = ctk.CTkButton(root, text="Старт", command=start_game, fg_color = "#650ffa")
start_btn.place(x=400, y=300)

# Кнопка, яка буде випадково змінювати положення
btn = ctk.CTkButton(root, text="Натисни мене", command=show_random_button, fg_color = "#1b0ffa")

# Прив’язка клавіші Esc до виходу з гри
root.bind("<Escape>", exit_game)

root.mainloop()