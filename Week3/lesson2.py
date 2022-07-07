# set1 = {
#     1,2,3,4,5,
# }
# set2 = {1,2,3,4,5,6}
# print(set1.union(set2))
# print(set1)
# set1 = {'Hello', 'banana'}
# set2 = {'Hello', 'apple', 'pineapple'}
# set3 = {'Hello', 'potato', 'orange'}
# # set1.update(set2)   #Добовляет слова, которых нет
# # print(set1)
# # print(set1.isdisjoint(set2)) #Возратит TRUE если нет похожих элементов. Не пересекающихся
# print(set1.intersection(set3, set2))  #Выводит только то, что есть во всех сетах. Только пересечение.

# set1 = {1,2}
# set2 = {3}
# set3 = {4,5}
# set4 = {3,2,6}
# set5 = {6}
# set6 = {7,8}
# set7 = {9,8}
#
# print(set1.intersection(set2, set3, set4, set5, set6, set7))
# set7.intersection_update(set6)
# b = (set5.intersection(set4, set3))
# c = (set2.intersection(set4))
# d = (set1.intersection(set4))
#
# set7.update(b)
# set7.update(d)
# set7.update(c)
# print(set7)

# x = {1,2,3,4,3,5,2}
# y = {1,2,3,4,5,6,7,8,9,11}
# if x.issuperset(y):
#     print('Объект x является супермножеством')
# else:
#     print('Cупермножества не обнаружены')
# if x == y:
#     print('Множества равны')

# Генератор списков list , dict
# lists = []
# for i in range(1, 10001):
#     lists.append(i)
# print(lists)
# str1 = "kkhlksfhhhkdskhf; jkhudhr; kjdxkjfh"
#
# # lists = [i for i in range(1, 10001)]
# lists = [i for i in str1]
# print(lists)

import datetime

# print(time_now)
# lists = []
# time_now = datetime.datetime.now()    #Вывести дату и время
# for i in range(1,10001):
#     lists.append(i)
# delta = datetime.datetime.now() - time_now
# print(delta)
# time_now = datetime.datetime.now()
# lists = [i for i in range(1, 10001)]
# delta = datetime.datetime.now() - time_now
# print(delta)
# lists = [i**2 for i in range(1, 10001) if i % 2 == 0 and i % 5 == 0]
# print(lists)

# Факториал числа

# number = int(input('Введите число: '))
# fact = 1
# for i in range(1, number +1):
#     fact *= i
# print(fact)
# ------------------------------------------
# dicts = {i: i**2 for i in range(1, 5)}
# print(dicts)

# lists = ['apple', 'banana']
# dict = {i: i*3 for i in lists}
# print(dict)
# --------------------------------------------
# Камень ножницы бумага (игра)


import random
while True:
    user_action = input("Сделайте выбор — камень, ножницы или бумага: ")
    possible_actions = ["камень", "бумага", "ножницы"]
    computer_action = random.choice(possible_actions)
    print(f"\n Вы выбрали {user_action}, компьютер выбрал {computer_action}.\n")
    if user_action == computer_action:
        print(f"Оба пользователя выбрали {user_action}. Ничья!!")
    elif user_action == "камень":
        if computer_action == "ножницы":
            print("Камень бьет ножницы! Вы победили!")
        else:
            print("Бумага оборачивает камень! Вы проиграли.")
    elif user_action == "бумага":
        if computer_action == "камень":
            print("Бумага оборачивает камень! Вы победили!")
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
    elif user_action == "ножницы":
        if computer_action == "бумага":
            print("Ножницы режут бумагу! Вы победили!")
        else:
            print("Камень бьет ножницы! Вы проиграли.")
    # а также обратите внимание на код ниже
    play_again = ""
    play_again = input("Сыграем еще? (д/н): ")
    if play_again.lower() != "д":
        break