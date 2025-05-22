import customtkinter as ctk

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + shift)% 26 + base)
        elif char.isdigit():
            encrypted_text += str((int(char)+ shift) % 10)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decipher(text, shift):
    decrypted_text = ""
    for char in text:
        if char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                decrypted_text += chr((ord(char) - base - shift) % 26 + base)
            elif char.isdigit():
                decrypted_text += str((int(char) - shift) % 10)
            else:
                decrypted_text += char
    return decrypted_text
    
def encrypt_action():
    try:
        shift = int(shift_input.get())
        text = input_box.get("1.0", "end-1c")
        result = caesar_cipher(text, shift)
        output_box.delete("1.0", "end")
        output_box.insert("1.0", result)
    except ValueError:
        output_box.delete("1.0", "end")
        output_box.insert("1.0", "❌ Введіть число для зсуву!")

def decrypt_action():
    try:
        shift = int(shift_input.get())
        text = input_box.get("1.0", "end-1c")
        result = caesar_decipher(text, shift)
        output_box.delete("1.0", "end")
        output_box.insert("1.0", result)
    except ValueError:
        output_box.delete("1.0", "end")
        output_box.insert("1.0", "❌ Введіть число для зсуву!")

ctk.set_appearance_mode("System")
root = ctk.CTk()
root.title("Cesar Шифратор")
root.geometry("500x500")

input_box = ctk.CTkTextbox(root, width = 450, height = 100)
input_box.pack(pady = 10)

shift_input = ctk.CTkEntry(root, placeholder_text = "Введіть зсув (наприклад, 3)", width = 200)
shift_input.pack(pady = 10)

encrypt_btn = ctk.CTkButton(root, text = "🔐 Зашифрувати", command = encrypt_action)
encrypt_btn.pack(pady = 5)

decrypt_btn = ctk.CTkButton(root, text = "🔓 Розшифрувати", command = decrypt_action)
decrypt_btn.pack(pady = 5)

output_box = ctk.CTkTextbox(root, width = 450, height = 100)
output_box.pack(pady = 20)

root.mainloop()
