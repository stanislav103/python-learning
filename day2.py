import json

# Функция которая принимает список чисел и возвращает только чётные
def filter_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

# 
# Словарь с данными о пользователе (имя, возраст, город) — выведи красиво

user = {
    "name": "Станислав",
    "age": 34,
    "city": "Одесса"
}

print(f"Имя: {user['name']}")
print(f"Возраст: {user['age']}")
print(f"Город: {user['city']}")

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(user, f, ensure_ascii=False, indent=2)

with open("user.json", "r", encoding="utf-8") as f:
    loaded_user = json.load(f)

print(loaded_user)
print(loaded_user["name"])