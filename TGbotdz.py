import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("TOKEN")

# Список цікавих фактів
space_facts = [
    "У космосі так багато зірок, що їх неможливо порахувати.",
    "Найближча зірка до нашої планети — це Сонце.",
    "У космосі немає звуку, тому що там немає повітря.",
    "Юпітер — найбільша планета Сонячної системи."
]

country_facts = [
    "Найбільш густонаселена країна у світі — Індія.",
    "Найменша країна у світі — Ватикан.",
    "Канада має найбільшу кількість озер у світі.",
    "Україна — найбільша країна в Європі за площею."
]

# Обробка команди /start
@bot.message_handler(commands=["start"])
def send_welcome(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Привіт")
    button2 = KeyboardButton("Почати")
    keyboard.add(button1, button2)
    
    bot.send_message(message.chat.id, "Привіт, я бот, який може розповісти тобі цікаві факти!", reply_markup=keyboard)

# Обробка натискання кнопок з клавіатури
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "Привіт":
        bot.send_message(message.chat.id, "Привіт! 😃")

    elif message.text == "Почати":
        keyboard = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton("Розповісти факт про космос", callback_data="space_fact")
        button2 = InlineKeyboardButton("Розповісти факт про країну", callback_data="country_fact")
        keyboard.add(button1, button2)
        
        bot.send_message(message.chat.id, "Обери, про що хочеш дізнатися:", reply_markup=keyboard)

    else:
        bot.send_message(message.chat.id, "Я не знаю такої відповіді. Спробуй натиснути на кнопку.")

# Обробка inline-кнопок
@bot.callback_query_handler(func=lambda call: True)
def handle_inline_buttons(call):
    if call.data == "space_fact":
        fact = random.choice(space_facts)
        bot.send_message(call.message.chat.id, f"✨ Факт про космос: {fact}")

    elif call.data == "country_fact":
        fact = random.choice(country_facts)
        bot.send_message(call.message.chat.id, f"🌍 Факт про країну: {fact}")

# Запуск бота
bot.polling()