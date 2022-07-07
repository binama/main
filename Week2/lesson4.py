# tuple  не изменяемый тип данных (кортеж)
# tuples = (1, 2, 3)
# print(type(tuples))  # Узнать какая эта функция
# print(tuples)
# print(tuples[2])     # Достать элемент
# tuples1 = tuple()
# tuples2 = (1, )
# print(type(tuples2))
# for i in tuples:
#     print(i+2)
# print(len(tuples))

# Dictionary  (Словари)
# dict_1 = {
#     "name1": ["Nazgul", "Vadim"],
#     "name2": "Mirlan",
#     "name3": "Andrew",
# }
# print(dict_1['name1'])
# dict_1['name2'] = "Yasir"
# dict_1['name1'].append('Ulan')
# print(dict_1)

# items() Метод (отображает ключ и значение)

# for i in dict_1.items():
#     print(i)

# values() Метод (отображает только значения)
# for i in dict_1.values():
#     print(i)

# keys() Только ключ отображает
# for i in dict_1.keys():
#     print(i)

# print(type(dict_1.keys()))
# print(dict_1.values())
# dict_1 = {
#     "name1": ["Nazgul", "Vadim"],
#     "name2": "Mirlan",
#     "name3": "Andrew",
# }
# dict_1['name4'] = "Kunduz"  # Добавление в словарь ключа
# print(dict_1)

# Подсчитать средний бал студентов.
# students = {
#     "Ulan": 98,
#     "Kunduz": 90,
#     "Vadim": 99,
#     "Nurdin": 100,
# }
# other = {
#     "Tanuru": 88,
#     "Azamat": 78,
# }
# students.update(other)  # Добавили новых студентов Тануру и Азамат
# print(students)
# result = sum(students.values()) / len(students) # Средний бал
# print(result)

# UPDATE() Метод который обновляет

# after_exam = {}
# for key, values  in students.items():  #Список студентов с оценками - 2
#     # print(key, values)
#     val = values - 2
#     after_exam.update(
#         {key: val}
#     )
# print(after_exam)

# FROM KEYS Метод который делает ключи из листа и всем добавляет одинаковое значение.
# lists = ["book1", "table", "board"]
# dicts = dict().fromkeys(lists, 20)
# # dicts.clear()  # Очищает лист
# dicts_1 = dicts.copy(  # Копирует данные в диктс1
# print(dicts_1)

# other = {
#     "Tanuru": 88,
#     "Azamat": 78,
# }
# another = other.copy()
# other["Tanuru"] = 100
# print(another)
# print(id(another))
# print(id(other))


# tovar = {
#     "Albeni": 40,
#     "Snickers": 45,
#     "Mars": 60,
#     "Twix": 80,
#     "Baunti": 100,
# }
# name = input('Введите название товара: ')
# if name in tovar:
#     print(items.tovar)
# else:
#     print('Нет такого товара')

# products = {}
#
# for i in range(2):
#     product_name = input('Введите название продукта: ')
#     product_price = int(input('Введите цену: '))
#     products[product_name] = product_price
#
#
# # search_value = input("Введите название продукта: ")
# # if search_value in products.keys():
# #     print(f'Имя продукта: {search_value}, price: {products[search_value]}')
# # else:
# #     print('Не найден продукт')
#
# # Выводит продукт ниже определенной цены
# min_value = int(input('Enter price: '))
# for key, value in products.items():
#     if value < min_value:
#         print(f'Имя продукта: {key}, price: {value}')

# Домашнее задание.
# Задача №1
# Из Dictionar №1: Добавьте в меню напитки, как ключ "drinks"
# А список всех доступных напитков: ['Coca-Cola', 'Sprite', 'Fanta'] как его значение.
# menu = {
#     'lagman': 120,
#     'plov': 120,
#     'borsh': 100,
# }
# menu2 = {
#     'drinks1': 'Coca-Cola',
#     'drinks2': 'Sprite',
#     'drinks3': 'Fanta',
# }
# menu.update(menu2)
# print(menu)

# Задача №2.
# Создайте пустой словарь. Запустите цикл, который 3 раза
# спросит его имя и его пароль. Записывайте имя пользователя, как ключ,
# а пароль, как его значение.
#
# slovar = {}
# for i in range(3):
#     slovar_login = input('Введите логин: ')
#     slovar_password= input('Введите пароль: ')
#     slovar[slovar_login] = slovar_password
# for login,password in slovar.items():
#     print(f'Логин: {login}, Пароль: {password}')
# print(slovar)

# Задача №3
# Создайте Словарь с 5-ю элементами, где ключи это их имена, а значение, это их
# профессия. С помощью цикла ФОР выведите на экран строку:
# "Здравствуйте .Имя. Прекрасная профессия .Профессия."

# slovar = {
#     'Иван': 'Сварщик',
#     'Василий': 'Водитель',
#     'Ольга': 'Продавец',
#     'Мария': 'Политик',
#     'Виктор': 'Сталкер',
# }
# values = slovar.values  # znacheniya
# key = slovar.keys  # kluch
# for key , value in range(5):
#     print(f'Здравствуйте {key} Прекрасная профессия {value}')
