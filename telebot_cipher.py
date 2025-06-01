import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = ":)"
bot = telebot.TeleBot(TOKEN)

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

user_states = {}

def encrypt_masonic(text, lang):
    used_dict = cipher_dict if lang == "Кирилиця" else latin_key
    return ''.join(used_dict.get(char.upper(), char) for char in text)

def decrypt_masonic(text, lang):
    used_dict = cipher_dict if lang == "Кирилиця" else latin_key
    reverse_dict = {v: k for k, v in used_dict.items()}
    return ''.join(reverse_dict.get(char, char) for char in text)

def cesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def cesar_decipher(text, shift):
    return cesar_cipher(text, -shift)

@bot.message_handler(commands = ['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привіт, Обери тип шифрування:", reply_markup=main_menu())

def main_menu():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("🔐 Шрифт Цезаря", callback_data="cesar"),
               InlineKeyboardButton("🕵️ Масонський", callback_data="masonic"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    user_id = call.message.chat.id
    state = user_states.get(user_id, {})

    if call.data in ['cesar', 'masonic']:
        state['cipher'] = call.data
        bot.send_message(user_id, "Оберіть мову:", reply_markup = lang_menu())

    elif call.data in ['Кирилиця', 'Латиниця']:
        state['lang'] = call.data
        user_states[user_id] = state
        if state['cipher'] == 'cesar':
            bot.send_message(user_id, "Введіть зсув (число):")
        else:
            bot.send_message(user_id, "Введіть текст для шифрування або розшифрування:")

    state['awaiting_input'] = True
    user_states[user_id] = state

    bot.answer_callback_query(call.id)

def lang_menu():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("Кирилиця", callback_data = "Кирилиця"),
               InlineKeyboardButton("Латиниця", callback_data = "Латиниця"))
    return markup

@bot.message_handler(func = lambda message: True)
def text_handler(message):
    user_id = message.chat.id
    state = user_states.get(user_id)

    if not state or not state.get("awaiting_input"):
        return
    
    if state['cipher'] == 'cesar' and 'shift' not in state:
        try:
            shift = int(message.text.strip())
            state['shift'] = shift
            bot.send_message(user_id, "Тепер введіть текст для шифрування або розшифрування:")
            user_states[user_id] = state
            return
        except ValueError:
            bot.send_message(user_id, "❌ Введіть коректне число!")
            return
        
    text = message.text.strip()
    lang = state.get('lang')
    if state['cipher'] == 'caesar':
        shift = state.get('shift', 3)
        encrypted = cesar_cipher(text, shift)
        decrypted = cesar_decipher(encrypted, shift)
    else:
        encrypted = encrypt_masonic(text, lang)
        decrypted = decrypt_masonic(encrypted, lang)

    response = f"🔐 Зашифровано: {encrypted}\n🔓 Розшифровано: {decrypted}"
    bot.send_message(user_id, response)
    user_states[user_id] = {}

bot.infinity_polling()