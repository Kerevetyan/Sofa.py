# Окрім того що я додала декілька тем, я зробила так щоб при натискані на кнопку зявлявся спалах на 1/10 секунди
import tkinter as tk

current_expression = ""
def on_button_click(button, btn_widget):
    global current_expression

    btn_widget.config(bg="lightblue")###

    if button == "C":
        current_expression = ""
        display.delete(0, tk.END)

    elif button == "=":
        try:

            result = eval(current_expression)
            display.delete(0, tk.END)
            display.insert(0, str(result))
            current_expression = str(result)

        except Exception:
            
            display.delete(0, tk.END)
            display.insert(0, "Помилка")
            current_expression = ""

    else:

        current_expression += str(button)
        display.insert(0, tk.END)
        display.insert(0, current_expression)

    root.after(100, lambda: btn_widget.config(bg="lightgray"))###

def set_theme(theme):
    if theme == "light":
        root.config(bg = "white")
        display.config(bg = "lightgray", fg = "black")
    elif theme == "dark":
        root.config(bg = "black")
        display.config(bg = "gray", fg = "white")
    elif theme == "purple":
        root.config(bg = "purple")
        display.config(bg = "#D8BFD8", fg = "black")
    elif theme == "yellow":
        root.config(bg = "yellow")
        display.config(bg = "black", fg = "white")
    elif theme == "blue":
        root.config(bg = "blue")
        display.config(bg = "#77d8e0", fg = "white")
    for button in buttons:
        button.config(bg = "lightgray" if theme == "light" else "darkgray" if theme == "dark" else "gray",
                       fg = "black" if theme != "dark" else "white")
        
root = tk.Tk()
root.title("Калькулятор")
root.geometry("400x600")

display = tk.Entry(root, font = ("Arial", 24), justify = "right")
display.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

# Кнопки калькулятора
buttons = []
button_texts = [
'7', '8', '9', '/',
'4', '5', '6', '*',
'1', '2', '3', '-',
'C', '0', '=', '+'
]

row_val = 1
col_val = 0

# Створюємо кнопки
for text in button_texts:

    button = tk.Button(root, text = text, font = ('Time New Romance', 18), width = 5, height = 2)
    button.grid(row = row_val, column = col_val)
    button.config(command=lambda t=text, b=button: on_button_click(t, b))###
    buttons.append(button)
    col_val += 1
    if col_val > 3:

        col_val = 0
        row_val += 1

# Меню
menubar = tk.Menu(root)
theme_menu = tk.Menu(menubar, tearoff = 0)
theme_menu.add_command(label = "Світла тема", command = lambda: set_theme("light"))
theme_menu.add_command(label = "Темна тема", command = lambda: set_theme("dark"))
theme_menu.add_command(label = "Фіолетова тема", command = lambda: set_theme("purple"))
theme_menu.add_command(label = "Жовта тема", command = lambda: set_theme("yellow"))
theme_menu.add_command(label = "Синя тема", command = lambda: set_theme("blue"))
menubar.add_cascade(label = "Налаштування", menu = theme_menu)

root.config(menu = menubar)
root.mainloop()