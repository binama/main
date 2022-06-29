# Условные операторы

# a = [2, 3, 4]
# s = 'String'
# a.reverse()
# s.lower()
# print(a)
# print(s.lower())   # Маленькими буквами печатает

# IF
# num1 = int(input('num 1: = '))
# num2 = int(input('num 2: = '))
# if num1 > num2:
#     print('{0} grater {1}'.format(num1, num2))
# elif num2 > num1:
#     print('{0} grater {1}'.format(num2, num1))

# Kalkulyator
# num1 = int(input('num 1: = '))
# num2 = int(input('num 2: = '))
# operator = input('operator: ')
#
# if operator == '+':
#     result = num1 + num2
#     print('result = {}'.format(result))
# elif operator == '-':
#     result = num1 - num2
#     print('result = {}'.format(result))
# else:
#     result = num1 / num2
#     print('result = {}'.format(result))

# lists = [1, 2]
# lists = [ 1, 2, 3, 4]
#
# if 3 in lists:
#     print('Hello')

# or and

# lists = [18, 22, 25, 6]
# # if (22 in lists) and (25 in lists):
# #     print('yes')
# if (200 in lists) or (10 in lists):
#     print('yes')

# Создание числового списка при помощи list() и range()
# a = list(range(1, 1001))
# result = []
# # print(a)
# for i in a:
#     if  i % 15 == 0:
#         # print(i, 'Kratno 3, 5, and 15')
#         result.append(i)
# print(result)

# temper = float(input('Введите температуру: '))
# if temper < -273.15:
#     print('Температура недействительна')
# elif temper == -273.15:
#     print('Температура равна НУЛЮ')
# elif temper == 0:
#     print('Точка замерзания')
# elif temper > 0 and temper < 100:
#     print('Температура находится в нормальном диапозоне')
# elif temper == 100:
#     print('Температура в точке кипения')
# elif temper > 100:
#     print('Температура выше точки кипения')
# edenica = (input('F or C ?  '))
# if edenica == 'f':
#     print((9 / 5) * (temper+ 32))
# elif edenica =='c':
#     print((5 / 9) * (temper - 32))

# Tablica umnojenyaa

# number = int(input("Enter a number: "))
# print("Tablica: ", number)
# for count in range(1, 11):
#    print(number, 'x', count, '=', number * count)

# num = int(input('enter a nuber: '))
# slovo = 'Python'
# for i in range(1, len(slovo) + 1):
#     print(slovo)


slovo = 'Python'

for i in range(1, 6 +1):
    print(i)
