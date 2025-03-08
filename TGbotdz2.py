'''import telebot
import schedule
import time
import datetime

# TOken
TOKEN = ""
bot = telebot.TeleBot(TOKEN)

# user ID
CHAT_ID =  #ID чату (@userinfobot)

# налаштування розкладу
def send_reminder():
    bot.send_message(CHAT_ID, "Час зробити важливу справу")

# Я часто забуваю зарядити навушники
def send_reminder1():
    bot.send_message(CHAT_ID, "Поставити навушники на зарядку")

# Бот вітає з новим роком)
def send_reminder2():
    bot.send_message(CHAT_ID, "Зустрічаємо новий 2222 рік!")

def new_year_greeting():
    today = datetime.date.today()
    if today.month == 1 and today.day == 1:  # Перевіряємо, чи сьогодні 1 січня
        send_reminder2()

# заплановані нагадування
schedule.every().day.at("09:00").do(send_reminder)
schedule.every().day.at("18:00").do(send_reminder)
schedule.every().day.at("15:55").do(send_reminder1)
schedule.every().day.at("00:00").do(new_year_greeting)
schedule.every(10).seconds.do(send_reminder)

# Основний цикл
while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        print(f"Помилка: {e}")
        time.sleep(5)'''



'''import telebot

TOKEN = ""

bot = telebot.TeleBot(TOKEN)
chat_id = 

def convert_unit(value, from_units, to_units):
    conversions = {
        "чашки": {"мілілітри":240},
        "столових_ложок": {"мілілітри":15},
        "чайних_ложок": {"мілілітри":5},
        "склянки": {"мілілітри":250},
        "каструлі": {"мілілітри":1000},
        "ополоників": {"мілілітри":236}
    }
    if from_units in conversions and to_units in conversions[from_units]:
        return value * conversions[from_units][to_units]
    else:
        return None
@bot.message_handler(commands=["start"])
def send_hello(message):
    bot.send_message(message.chat.id, "Привіт, я допоможу тобі конвертувати задану кількість чашок, ложок, склянок, каструль, ополоників в мілілітри. \
                      \nНапиши в такому форматі: 5 чашки в мілілітри.")
@bot.message_handler(func = lambda message: True)
def handle_message(message):
    text = message.text.lower()
    try:
        parts = text.split(" в ")
        value_and_from_unit = parts[0].split()
        to_unit = parts[1]
        value = float(value_and_from_unit[0])
        from_unit = value_and_from_unit[1]
        result = convert_unit(value, from_unit, to_unit)
        if result is not None:
            bot.send_message(message.chat.id, f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            bot.send_message(message.chat.id, "перепрошую спробуйте ще раз")
    except Exception as e:
        bot.send_message(message.chat.id, "Все погано у тебе помилка в коді")
bot.polling()'''