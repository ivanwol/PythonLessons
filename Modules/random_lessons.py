import random

# from random import randint

# number = random.random()
# print(int(number * 100))

# number = random.randint(49, 50)
# print(number)

# number = random.randrange(2, 10, 3)
# print(number)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# random.shuffle(numbers)
# print(numbers)

# a = random.choice(numbers)
# print(a)

# number = random.randint(1, 10)
# print(number)
# if number > 5:
#     print("Победа")
# else:
#     print("Поражение")

# numbers = [1] * 9
# numbers.append(10)
# while True:
#     try:
#         chance = (numbers.count(10) / len(numbers)) * 100
#         print("Шанс равен", chance, "%")
#         b = int(input("Введите (1) для продолжения или (2) для стопа: "))
#         if b == 1:
#             a = random.choice(numbers)
#             if a == 1:
#                 print(a)
#                 print("Поражение")
#                 numbers.append(10)
#                 numbers.remove(1)
#                 print(numbers)
#             else:
#                 print(a)
#                 print("Победа")
#                 break
#         elif b == 2:
#             print("Конец")
#             break
#         else:
#             print("Что то пошло не так")
#             break
#     except ValueError:
#         print("Введите целое !число!")

# a1 = input("Введите пятизначное число: ")
# numbers = []
# for i in a1:
#     numbers.append(int(i))
# a = numbers[0]
# c = numbers[2]
# e = numbers[4]
# print(e - a * c)




def funct1():
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    x = input("Введите знак(*, /, +, -): ")
    operations = {
        "+": num1 + num2,
        "-": num1 - num2,
        "/": num1 / num2,
        "*": num1 * num2
    }
    return operations.get(x), x, num1, num2


info = funct1()


def funct2(a):
    stroka = ""
    z = a[2], a[1], a[2], "=", a[0]
    for i in z:
        stroka = stroka + str(i)
    return stroka


print(funct2(info))