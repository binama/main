# Функии
# def test_func():
#     print('Hello world')
#
# test_func()

# def test_fubc():
#     pass

# summ = int(input('Введите сумму: '))
# year = int(input('На какой срок: '))
# precent = float(input('Процент: '))
#
# precent_one_year = summ * precent
# all_cash = precent_one_year * year + summ
# print(all_cash)

# def get_cash(summ, year, precent):
#     precent_one_year = summ * precent
#     all_cash = precent_one_year * year + summ
#     print(all_cash)
#     return all_cash
#
# get_cash(100000, 5, 0.2)                        # Вызвать функцию

# def get_cash_2(summ, year, precent):
#     precent_one_year = summ * precent
#     all
#
# def get_cash_2(summ, year):
#     # summ = int(input(' Vvvedite summu: '))
#     # year = int(input('Vvedite na skolko let: '))
#     summa = summ * 1.1 ** year
#     print(summa)
#     return summa
#
# get_cash_2(1000, 2)


# # Найти в слове букву
# def find_index(word, letter):
#     list_index = []
#     for i in range(len(word)):
#         if word[i].lower == letter.lower:
#             list_index.append(i)
#     return list_index
#
# print(find_index('nonono', 'o'))

# Крестики нолики
lists = []
count = 0
tik_tak = [["o", 0, "x"], [0, 0, "x"], ["x", 0, "o"]]
for i in range(len(tik_tak)):
    for j in range (len(tik_tak[i])):

        if tik_tak[i][j] == 0:
            lists.append((i, j))
            # count += 1
print(lists)
