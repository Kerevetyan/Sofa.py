import random

choices = []
print("Введіть свої варіанти рішень (введіть 'stop' для завершення):")

while True:
    choice = input("Введіть варіант: ")
    if choice.lower() == 'stop':
        break
    elif choice.strip():
        choices.append(choice)
    else:
        print("Введено порожній варіант, спробуйте ще раз.")

if not choices:
    print("Ви не ввели жодного варіанту! Запускаємо ще раз...")

print(choices)

with open('file.txt', "w", encoding="utf-8") as file:
    for choice in choices:
        file.write(choice + "\n")

if choices:
    selected_choice = random.choice(choices)
    print(f"Випадково обраний варіант: {selected_choice}")
else:
    print("Список варіантів порожній. Спробуйте ще раз.")
