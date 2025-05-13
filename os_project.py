
'''import pandas as pd

df = pd.read_csv("disney_princess.csv")

print(df)
print(df.head())
print(df.columns)
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.dropna())
print(df.dropna(how='all'))
print(df.dropna(subset=['HairColor', 'EyeColor']))


import pandas as pd

df = pd.read_csv("disney_princess.csv")
print(df[df['PopularityScore']<80][['FirstMovieTitle','FirstMovieYear','NumberOfSongs']])
print(df[df['PopularityScore']>80])


print(df.groupby('HairColor')['PopularityScore'].mean())
print(df.groupby('EyeColor')['MovieRuntimeMinutes'].mean())
print("---------------")
print(df.sort_values('PopularityScore')[['FirstMovieTitle', 'PopularityScore']])
print("------------------")
print(df.sort_values('PopularityScore', ascending=False)[['FirstMovieTitle', 'PopularityScore']])
print(df.sort_values('FirstMovieYear').head(7)[['FirstMovieTitle', 'FirstMovieYear']])
print(df[df['FirstMovieYear']==2010][['FirstMovieTitle','FirstMovieYear','PopularityScore']])

df2 = pd.read_csv("disney_princess.csv")
print(df2[df2['FirstMovieYear']==1967])
print(df2[df2['NumberOfSongs']==0])
print(df2[df2['PrincessName']=="Mulan"][['FirstMovieYear','CulturalOrigin']])'''

#1
'''import matplotlib.pyplot as plt

week_days = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'Пятниця', 'Субота', 'Неділя']
views = [0, 10, 12, 16, 30, 50, 80]

plt.plot(week_days, views)  
plt.title("Зростання цін за тиждень")
plt.xlabel("День тижня")
plt.ylabel("Ціни")
plt.show()'''
#2
'''import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("disney_princess.csv")
brazil_data = df[df['PrincessName'] == 'Anna']
plt.figure(figsize=(10,6))
plt.plot(brazil_data['FirstMovieYear'], brazil_data["PopularityScore"], marker = 'o',color= 'b')
plt.title('Популярність Принцеси Анни за роком виходу фільму', fontsize=14)
plt.xlabel('Рік', fontsize=12)
plt.ylabel('Популярність Принцеси', fontsize=12)
plt.grid(True)
plt.show()'''

#3
'''import matplotlib.pyplot as plt

categories = ['God of war', 'Devil May cry', 'STALKER', 'The last of us', 'Fortnite', 'Resident Evil']

values = [49, 10, 35, 45, 42, 49]

colors = ['red', 'blue', 'green', 'purple', 'orange', 'red']
plt.bar(categories, values, color=colors)

plt.xlabel('Ігри')
plt.ylabel('Популярність')
plt.title('Порівняння популярності ігор')

plt.show()'''

#4
'''import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("disney_princess.csv")
# Підрахунок кількості мільярдерів у кожній індустрії
industry_counts = df["CulturalOrigin"].value_counts()
# Побудова стовпчастої діаграми
plt.figure(figsize=(12, 6))
plt.bar(industry_counts.index, industry_counts.values, color="pink")

plt.xlabel("Походження")
plt.ylabel("Кількість принцес")
plt.title("Розподіл принцес за походженням")
plt.xticks(rotation=90)

plt.show()'''

#5
'''import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("disney_princess.csv")
FirstMovieYear_counts = df["FirstMovieYear"].value_counts()

top_industries = FirstMovieYear_counts[:35]
top_industries["Інші"] = FirstMovieYear_counts[35:].sum()

plt.figure(figsize=(8, 8))
plt.pie(
top_industries,
labels=top_industries.index,
autopct="%1.1f%%", # Додаємо відсотки
colors=plt.cm.Paired.colors, # Встановлюємо кольори
startangle=140 # Повертаємо діаграму
)
plt.title("Розподіл дати випуску фільмів")
plt.show()'''