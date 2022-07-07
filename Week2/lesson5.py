            # Методы

# other = {
#     "Tanuru": 88,
#     "Azamat": 78,
#     "Yryskeldi": 100,
# }
# print(other.get("Yryskeldi", True)) # Получить значение любое Метод гет
# print(other['Yryskeldi'])
# print(other.setdefault("Aza", 86)) # Если ключа нет, он его создает
# print(other)
# # removed = other.pop("Tanuru")  # Удаляет ключб но оставляет его значение
# removed = other.popitem()    # Удаляет любой элемент произвольный рандомно
# print(removed)
# other[removed[0]] = removed[1] # Возвратили обратно удаленный элемент
# print(other)

# # СРЕДНИЙ БАЛ
# students = {
#     "Andrei": {
#         "int": 50,
#         "str": 77,
#         "if": 90
#     },
#     "Mirlan": {
#         "int": 70,
#         "str": 75,
#         "if": 87
#     },
#     "Aidar": {
#         "int": 99,
#         "str": 95,
#         "if": 98
#     },
#     "Bekbolsun": {
#         "int": 65,
#         "str": 67,
#         "if": 66
#     }
# }
# avg = {}  # Средний бал
# for i in students:
#     val = sum(students[i].values()) / len(students[i].values())
#     avg.update(
#         {
#             i: val
#         }
#     )
# print(avg)

# i = 0
# while i < 10:
#     print(i)
#     i += 1

# while True:       #Бесконечный цикл
#     print('Hello')

# while True:         #Проверка на слово СТОп и выход из цикла
#     i = input('Введите число: ')
#     if i.lower() == "stop":
#         print('Bye bye')
#         break

# Програ проверки пароля в базе
# Lists = ['351', '352', '353']
# counter = 0  # Счетчик
# while True:
#     i = input('Введите пароль: ')
#     counter += 1
#     if i in Lists:
#         print('ok')
#         break
#     if counter == 3:
#         print('Много попыток')
#         break

# Программа игра Поле Чудес
# cities = ["Bishkek", "Tashkent", "New-York", "Paris", "Moscow"]
# from random import choice
# a = choice(cities)
# count = 0
# print(a)
# while True:
#     i = input('Введите букву: ')
#     count += 1
#     if i in (a):
#         print('Есть такие буквы', a.find(a))
#         print(a)
#         break
#     if count == 3:
#         print('Много попыток')
#         break



# import random
#
# # создать список слов
# wordList = ["bishkek", "tashkent", "paris", "moscow", "new-york"]
# # wordList = ["Bishkek", "Tashkent", "New-York", "Paris", "Moscow"]
#
# # создать пустой список для хранения используемых букв
# wordChosen = random.choice(wordList)
#
# # создать пустой список для хранения используемых букв
# used = []
#
# # создать переменную для хранения и отображения догадок игрока
# display = wordChosen
# for i in range(len(display)):
#     # замените каждую букву на '_'
#     display = display[0:i] + "_" + display[i + 1:]
#
# # поставить пробел между каждым тире
# print(" ".join(display))
#
# # счетчик останавливает игру, как только все буквы были угаданы правильно
# attempts = 0
#
# # продолжайте спрашивать игрока, пока все буквы не будут угаданы
# while display != wordChosen:
#     guess = input("Пожалуйста введите букву: ")
#     guess = guess.lower()
#     # Добавить догадки игроков в список используемых букв
#     used.extend(guess)
#     print("Попыток: ", attempts)
#
#     # Поиск по буквам в ответе
#     for i in range(len(wordChosen)):
#         if wordChosen[i] == guess:
#             display = display[0:i] + guess + display[i + 1:]
#
#     print("Используемые буквы: ", used)
#     # print(used)
#
#     # Выведите строку с угаданными буквами (с пробелами между ними))
#     print(" ".join(display))
#     attempts = attempts + 1
#
# print("Молодец, ты угадал!")

# cities = ["Bishkek", "Tashkent", "New-York", "Paris", "Moscow"]
# chosen_city = random.choice(cities).lower()
# letters_list = []
# word =['-'] * len(chosen_city)

