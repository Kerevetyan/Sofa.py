'''films = "INTERSTELLAR, AVATAR, SPIDER-MAN"
with open ("text.txt", "w") as file:
    file.write(films)
    print("Фільми записані у файл")

with open("write.txt", "r") as file:
    text = file.readline()
    print(text)'''


'''import os

file_path = "data.txt"

# Перевірка чи файл існує
if os.path.exists(file_path):
    size = os.path.getsize(file_path)
    print(f"Розмір файлу: {size} байт")

    if size > 1024:
        print("Файл занадто великий!")
else:
    print("Файл не знайдено.")'''


'''import os

# Шлях до папки
folder = "temp_data"
filename = "fifi.tmp"
# Перевірка, чи існує така папка
if os.path.exists(folder):
    for filename in os.listdir(folder):
        # Повний шлях до файлу
        file_path = os.path.join(folder, filename)
        
        # Якщо це файл і закінчується на .tmp — видаляємо
        if os.path.isfile(file_path) and filename.endswith(".tmp"):
            os.remove(file_path)
            print(f"Файл {filename} видалено.")
else:
    print("Папка temp_data не знайдена.")'''

'''import os

# Отримуємо список усіх елементів у поточному каталозі
files = [f for f in os.listdir() if os.path.isfile(f)]

# Створюємо список кортежів (ім'я файлу, розмір)
files_with_size = [(f, os.path.getsize(f)) for f in files]

# Сортуємо список за розміром у зворотному порядку
files_with_size.sort(key=lambda x: x[1], reverse=True)

# Виводимо результат
print("Файли у каталозі, відсортовані за розміром (від найбільшого до найменшого):")
for name, size in files_with_size:
    print(f"{name}: {size} байт")'''
