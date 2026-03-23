print("Привет! Это мой первый файл day1.py")
print("Python 3.14 работает отлично")

name = input("Как тебя зовут? ")
print("Круто,", name, "! Начинаем путь в Python 🚀")

# После ввода имени
age = int(input("Сколько тебе лет? "))
if age >= 18:
    print("Взрослый кодер — можно всю ночь! 😎")
else:
    print("Юный гений начинает путь 🚀")

film = input("Любимый фильм? ")
print("В верхнем регистре:", film.upper())
print("Длина названия:", len(film), "символов")

# Мини-игра
secret = 7
guess = int(input("Угадай число от 1 до 10: "))
if guess == secret:
    print("Красавчик! Угадал!")
elif guess > secret:
    print("Меньше!")
else:
    print("Больше!")