import customtkinter as ctk
import datetime
import requests

def fetch_horoscope(sign: str, day: str = "today"):
    url = "https://aztro.sameerkumar.website/"
    params = {"sign": sign.lower(), "day": day}
    response = requests.post(url, params = params)
    response.raise_for_status()
    return response.json()

app =ctk.CTk()
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

app.mainloop()