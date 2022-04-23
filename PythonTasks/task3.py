# def print_name():
#     a = input("Введите свое имя: ")
#     print("Меня зовут", a)
#
#
# print_name()
# print(a)

# PI = 3.14
#
#
# def s_circle():
#     r = int(input("Введите радиус круга: "))
#     s = PI * r ** 2
#     print(s)
#
#
# s_circle()

# try:
#     obj1 = input("Введите строку: ")
#     obj2 = input("Введите строку: ")
#     if type(int(obj1)) != int or type(int(obj2)) != int:
#         strin = obj1 + obj2
#         print(strin)
#     else:
#         suma = int(obj1) + int(obj2)
#         print(suma)
# except Exception:
#     print("Ошибка")

# try:
#     obj1 = input("Введите строку1: ")
#     obj2 = input("Введите строку2: ")
#     print(int(obj1) + int(obj2))
# except ValueError:
#     print(obj1 + obj2)
# season_choose = input("Введите номер месяца:")
#
#
# def season(m):
#     seasons = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
#     if m in seasons[0:1] or m in seasons[11]:
#         print("Зима")
#     elif m in seasons[2:5]:
#         print("Весна")
#     elif m in seasons[5:8]:
#         print("Лето")
#     elif m in seasons[8:11]:
#         print("Осень")
#     else:
#         print("Недопустимый номер месяца")

# sentence = input("Введите предложение: ")
# edit = sentence.replace(",", "").split()
# print(max(edit, key=len))
# import random
#
# min_num = int(input("Введите нижний диапазон: "))
# max_num = int(input("Введите верхний диапазон: "))
# count = int(input("Введите количество элементов: "))
# lst = []
# for i in range(count):
#     lst.append(random.randrange(min_num, max_num))
# print(sorted(lst))
# lst.sort(reverse=True)
# print(lst)
a = int(input("Введите количество денег, которые хотите положить в банк: "))
b = int(input("Введите на сколько лет: "))


def money(amount, years):
    procents = 10
    after = amount * (1 + (procents / 100)) ** years
    return after


print(money(a, b))