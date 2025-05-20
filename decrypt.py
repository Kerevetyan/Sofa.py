import customtkinter as ctk

# Шифри
cipher_dict = {
    'А': '@', 'Б': '#', 'В': '$', 'Г': '%', 'Ґ': '&',
    'Д': '*', 'Е': '(', 'Є': ')', 'Ж': '+', 'З': '-',
    'И': '=', 'І': '_', 'Ї': '{', 'Й': '}', 'К': '[',
    'Л': ']', 'М': ':', 'Н': ';', 'О': "'", 'П': '"',
    'Р': '|', 'С': '/', 'Т': '7', 'У': '~', 'Ф': '^',
    'Х': '?', 'Ц': '!', 'Ч': '@', 'Ш': '#', 'Щ': '$',
    'Ь': '%', 'Ю': '^', 'Я': '&'
}

latin_key = {
    'A': '@', 'B': '#', 'C': '$', 'D': '%', 'E': '&', 'F': '*', 'G': '(',
    'H': ')', 'I': '!', 'J': '^', 'K': '_', 'L': '+', 'M': '~', 'N': '`',
    'O': '-', 'P': '=', 'Q': '{', 'R': '}', 'S': '[', 'T': ']', 'U': ';',
    'V': ':', 'W': '"', 'X': "'", 'Y': '<', 'Z': '>', ' ': ' '
}

# Основні функції
def encrypt(text, lang):
    encrypted_text = ""
    used_dict = cipher_dict if lang == "Кирилиця" else latin_key
    for char in text:
        if char.upper() in used_dict:
            encrypted_text += used_dict[char.upper()]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, lang):
    used_dict = cipher_dict if lang == "Кирилиця" else latin_key
    reverse_dict = {v: k for k, v in used_dict.items()}
    decrypted_text = ""
    for char in text:
        if char in reverse_dict:
            decrypted_text += reverse_dict[char]
        else:
            decrypted_text += char
    return decrypted_text

# Оновлення тексту
def update_text():
    input_text = text_input.get("1.0", "end-1c")
    lang = lang_var.get()
    encrypted = encrypt(input_text, lang)
    text_output.delete("1.0", "end")
    text_output.insert("1.0", encrypted)

def decrypt_text():
    input_text = text_input.get("1.0", "end-1c")
    lang = lang_var.get()
    decrypted = decrypt(input_text, lang)
    text_output.delete("1.0", "end")
    text_output.insert("1.0", decrypted)

# Головне вікно
ctk.set_appearance_mode("light")
root = ctk.CTk()
root.title("Масонський шифратор")
root.geometry("500x500")

# Текстовий ввід
text_input = ctk.CTkTextbox(root, width=450, height=100, fg_color="lightgrey")
text_input.pack(pady=20)

# Вибір мови (розкладки)
lang_var = ctk.StringVar(value="Кирилиця")
lang_menu = ctk.CTkOptionMenu(root, values=["Кирилиця", "Латиниця"], variable=lang_var)
lang_menu.pack(pady=5)

# Кнопки
encrypt_button = ctk.CTkButton(root, text="Шифрувати", command=update_text, fg_color="purple")
encrypt_button.pack(pady=10)

decrypt_button = ctk.CTkButton(root, text="Розшифрувати", command=decrypt_text)
decrypt_button.pack(pady=10)

# Вивід
text_output = ctk.CTkTextbox(root, width=450, height=100, fg_color="white")
text_output.pack(pady=20)

root.mainloop()
