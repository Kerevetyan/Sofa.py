import telebot
import random

bot = telebot.TeleBot('')

UPLOAD_FOLDER = r"C:\memes/"

memes = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg", "10.jpg", "11.jpg", "12.jpg", "13.jpg", "14.jpg", "15.jpg", "16.jpg", "17.jpg", "18.jpg", "19.jpg", "20.jpg", "24.jpg", "25.jpg", "26.jpg", "27.jpg", "28.jpg", "29.jpg", "30.jpg"]

reactions = ["АХХАХАХА, РЖАКА", "Хахахахаха, не смішно", "ГЕНІАЛЬНО, ХАХАХАХ", "Що це було?", "Цікаво, але не смішно"]

@bot.message_handler(commands = ["start"])
def send_welcome(message):
    bot.reply_to(message, "Я бот легендарна свинка! Я розповідаю жарти надсилаю меми та дуркую. Команда /info або /help щоб дізнатись більше")

# Команда help Відправляє повідомлення з підказками
@bot.message_handler(commands = ["help"])
def send_help(message):
    bot.reply_to(message, "Я можу допомогти тобі з командами: /start, /help, /info, /randomphrase, /telljoke, /meme, /photo, /count, Здається все😊")

@bot.message_handler(commands = ["telljoke"])
def tell_joke(message):
    jokes = ["Я розповім тобі правду хороший рузький - мертвий рузький", "Надоїло ходи до діда /randomphrase", "Стакан з водою дивиться на порожній і каже: ти прям як вилитий я", "Крінж короче"]
    bot.reply_to(message, random.choice(jokes))

@bot.message_handler(commands = ["info"])
def tell_info(message):
    bot.reply_to(message, "У мене також є багато різних команд через слеш, натисніть /help щоб побачити їх усі!")

@bot.message_handler(commands = ["randomphrase"])
def random_message(message):
    phrase = ["Ой у лузі червона калина", "ПЄНАПЛААААСТ", "Wake up to relity", "Ідеї закінчились іди до /telljoke", "Я тоже хочу шоколадку(", "9 чи 10"]
    bot.reply_to(message, random.choice(phrase))

@bot.message_handler(content_types=["photo"])
def recive_meme(message):
#Дістаємо інформацію про надісланий файл із мемом
    file_info = bot.get_file(message.photo[-1].file_id)
#Завантажуємо файл з мемом
    downloaded_file = bot.download_file(file_info.file_path)
# Зберігаємо мем на комп'ютері унікальним іменем
    file_name = str(len(memes)+1) + ".jpg"
    with open(UPLOAD_FOLDER + file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
#Додаємо назву мема в список memes
    memes.append(file_name)
    bot.reply_to(message, random.choice(reactions))

@bot.message_handler(commands = ['meme'])
def send_random_meme(message):
    if memes:
        meme = random.choice(memes)
        with open(UPLOAD_FOLDER + meme, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)

    else:
        bot.reply_to(message, "Мемів поки немає :(")

@bot.message_handler(commands=['count'])
def meme_count(message):
    if memes:
        memes_count = len(memes)
        bot.reply_to(message,  f"Додано мемів: {len(memes)}" if memes else "Мемів не знайдено!")

bot.polling()
