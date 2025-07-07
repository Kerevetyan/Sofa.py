'''import customtkinter as ctk
import datetime
import requests

def fetch_horoscope(sign: str, day: str = "today"):
    url = "https://aztro.sameerkumar.website/"
    params = {"sign": sign.lower(), "day": day}
    response = requests.post(url, params = params)
    response.raise_for_status()
    return response.json()

app = ctk.CTk()
app.geometry("400x400")
app.title("Гороскоп")

signs = ["Aries","Taurus","Gemini", "Cancer", "Leo", "Virgo",
         "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

combo = ctk.CTkComboBox(app, values = signs)
combo.set("Aries")
combo.pack(pady = 20)

result = ctk.CTkTextbox(app, width=350, height=200)
result.pack(pady = 10)

last_date = ""

def update_horoscope():
    global last_date
    today = datetime.date.today().isoformat()
    if last_date == today:
        return
    sign = combo.get()
    try:
        data = fetch_horoscope(sign)
        txt = f"Гороскоп для {sign} ({data['curent_date']}):\n\n"
        txt += data.get("description", "")
        result.delete('1.0', "end")
        result.insert("1.0", txt)
        last_date = today
    except requests.exceptions.RequestException:
        result.delete("1.0", "end")
        result.insert("1.0", "Сервіс тимчасово недоступний. Спробуйте пізніше")
    except Exception as e:
        result.delete("1.0", "end")
        result.insert("1.0", f"Помилка: {e}")

dtn = ctk.CTkButton(app, text = "Оновити прогноз", command = update_horoscope)
dtn.pack(pady = 5)

update_horoscope()

app.mainloop()'''

import customtkinter as ctk
import datetime
import random

HOROSCOPES = {
    "aries": [
        "Сьогодні ви знайдете нове натхнення.",
        "Не бійтеся брати на себе ініціативу.",
        "Успіх прийде завдяки вашій рішучості."
    ],
    "taurus": [
        "Стабільність — ваш головний козир.",
        "Приділіть увагу фінансам.",
        "Не ігноруйте поради друзів."
    ],
    "gemini": [
        "Сьогодні день для нових знайомств.",
        "Не варто сумніватися в собі.",
        "Інтуїція допоможе уникнути помилок."
    ],
    "cancer": [
        "Емоції сьогодні важливі як ніколи.",
        "Час для відпочинку та турботи про себе.",
        "Зверніться до родини — вони поруч."
    ],
    "leo": [
        "Ваше лідерство надихає інших.",
        "Сміливо демонструйте свої таланти.",
        "Увага до деталей сьогодні ключова."
    ],
    "virgo": [
        "Організованість принесе гарні плоди.",
        "Не бійтеся змін у розпорядку дня.",
        "Допомога іншим повернеться сторицею."
    ],
    "libra": [
        "Шукайте баланс у всьому.",
        "Дипломатичність вирішить конфлікт.",
        "Зверніть увагу на зовнішній вигляд."
    ],
    "scorpio": [
        "Сьогодні час для глибоких роздумів.",
        "Будьте обережні з секретами.",
        "Пристрасть — ваша сила й слабкість."
    ],
    "sagittarius": [
        "Приготуйтеся до несподіваних пригод.",
        "Оптимізм відкриє нові двері.",
        "Навчання принесе задоволення."
    ],
    "capricorn": [
        "Ваша працьовитість буде винагороджена.",
        "Сконцентруйтеся на довгострокових цілях.",
        "Час переглянути особисті пріоритети."
    ],
    "aquarius": [
        "Не бійтеся бути унікальним.",
        "Нові ідеї змінять ваше життя.",
        "Спілкування принесе несподівані відповіді."
    ],
    "pisces": [
        "Прислухайтеся до своїх снів.",
        "Творчість — ваш порятунок сьогодні.",
        "Будьте ніжними до себе й інших."
    ]
}

ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("400x400")
app.title("Локальний Гороскоп")
app.configure(bg = "#705b48")


signs = list(HOROSCOPES.keys())

combo = ctk.CTkComboBox(
    app,
    values=signs,
    fg_color= "#b1c1f0",
    text_color = "#000000",
    dropdown_fg_color = "#b1c1f0",
    dropdown_text_color = "#000000"
)

combo.set(signs[0])
combo.pack(pady=20)

result = ctk.CTkTextbox(
    app,
    width=350,
    height=200,
    fg_color = "#916ded",
    text_color = "#ffffff"
)

result.pack(pady=10)

def update_local_horoscope():
    sign = combo.get()
    today = datetime.date.today().isoformat()
    predictions = HOROSCOPES.get(sign, ["Немає даних."])
    prediction = random.choice(predictions)
    result.delete("1.0", "end")
    result.insert("1.0", f"Гороскоп для {sign.title()} ({today}):\n\n{prediction}")

btn = ctk.CTkButton(
    app,
    text="Оновити прогноз",
    command=update_local_horoscope,
    fg_color = "#86e1eb",
    hover_color = "#71bec7",
    text_color = "#ffffff")

btn.pack(pady=5)

update_local_horoscope()
app.mainloop()
