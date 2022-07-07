# SET - МНОЖЕСТВО (Содержит не изменяемые типы данных)
# set1 = {1, "Ulan", 4, 1}
# print(set1)
# set1 = set()
# # set1 = {}
# print(type(set1))

# set1 = {"Monday", "Thuesday", "Wensday"}
# for i in set1:
#     for j in i:
#         print(j)
# По буквам вывели. В столбик.

#Метод UNION() Объеденяет
# set1 = {"Monday", "Thuesday", "Wensday", "Saturday"}
# set2 = {"Saturday", "Friday", "Monday"}
# # s = set1.union({"Saturday", "Friday"})
# set1.add("Saturday")
# # set1.clear()
#
# # print(set1.difference(set2))  #SRAVNIVAET SETY I VIDAET CHEGO NET
# # print(set2.symmetric_difference(set1))
# # set2.symmetric_difference_update(set1)
# print(set2)


#МЕТОД DIR

# print(dir(set1))  # Podskazka

# str1 = {"a", "b", "c"}
# str2 = {"a", "b", "d"}
# pop_set = str1.pop()
# # str_set = str1.difference(str2)
# print(pop_set)
# print(str1)
# # print(str_set)
# str2.discard("f")  # UDALYAET ELEMENT
# str2.remove("a")     # UDALYAET ELEMENT S OSHIBKOY

# print(str2)

a = [1,2,3,4,6,8,9,9,7]
b = [1,6,7,9]
a1 = set(a)
b1 = set(b)
print(a1.issubset(b1))
# a1.intersection_update(b1)
# print(a1)
# print(a1.intersection(b1))  # Одинаковые элементы в двух листах
# b1 = set(b)
# print(a1.symmetric_difference(b1))
# print(a1.issubset(b1))  # Есть ли элементы а1 в б1
print(a1.issuperset(b1))  # Проверяет есть ли все элементы б1 в а1

