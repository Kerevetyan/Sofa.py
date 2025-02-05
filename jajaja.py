import tkinter as tk

def my_func():
    button.config(text = "Ви привітались:)")

def func2():
    label.config(font =("Calibri", 25), fg = "red")

def func3():
    text = entry.get()
    if text.strip():
        label.config(text = f"Привіт, {text}!", font = ("Arial", 18), fg = "black")

root = tk.Tk()
root.title("Greeting")
root.geometry("800x500")
label = tk.Label(root, text = "Напишіть своє ім'я", font = ("Arial", 20), fg = "blue")
label.pack()
button = tk.Button(root, text = "Привітатись", command=my_func, fg = "purple")
button.pack()
button2 = tk.Button(root, text = "Змінити колір надпису", command=func2, fg = "purple")
button2.pack()
entry = tk.Entry(root)
entry.pack()
button3 = tk.Button(root, text = "Натискай)", command=func3, fg = "violet")
button3.pack()

root.mainloop()

# прграма яка змінює колір фону

import tkinter as tk
import random

colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta", "lime"]

def change_color():
    root.config(bg=random.choice(colors))

root = tk.Tk()
root.title("Зміна кольору фону")
root.geometry("500x300")

label = tk.Label(root, text="Натисни кнопку, щоб змінити колір фону!", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Магія (змінити колір)", command=change_color, font=("Arial", 12))
button.pack(pady=10)

root.mainloop()
