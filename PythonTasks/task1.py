# night = int(input("Введите количество часов которые проспали ночью: "))
# day = int(input("Введите количество минут которые проспали днем: "))
# minutes = night * 60  # Перевод часв в минуты
# suma = minutes + day  # Нахождение суммы минут днем и ночью
# print(suma)

# x = int(input("Оптимальное время для его сна(минуты): "))
# hours = x / 60  # Перевод минут в часы
# minutes = x % 60  # Нахождение остатка(деление минуты на часы)
# print(int(hours))
# print(minutes)


from math import sqrt  # Импорт функции sqrt с библиотеки math


# print(sqrt(121))


# a = int(input("Длина первой стороны треугольника: "))
# b = int(input("Длина второй стороны треугольника: "))
# c = int(input("Длина третьий стороны треугольника: "))
# p = (a + b + c) / 2  # Нахождение полупериметра
# s = sqrt(p * (p - a) * (p - b) * (p - c))  # Нахождение площади треугольника за формулой Герона
# print(s)


# number = int(input("Введите число: "))
# if -15 < number <= 12 or 14 < number < 17 or 19 <= number:  # Проверка входит ли число в промежутки
#     print(True)
# else:
#     print(False)


# number1 = float(input("Введите число номер 1: "))
# number2 = float(input("Введите число номер 2: "))
# operation = input("Введите операцию(+, -, /, *, mod, pow, div): ")
# try:
#     if operation == "+":
#         print(number1 + number2)
#     elif operation == "-":
#         print(number1 - number2)
#     elif operation == "/":
#         print(number1 / number2)
#     elif operation == "*":
#         print(number1 * number2)
#     elif operation == "mod":
#         print(number1 % number2)  # Остаток при делении
#     elif operation == "pow":
#         print(number1 ** number2)  # Вознесение числа к степени
#     elif operation == "div":
#         print(number1 // number2)  # Целочисленое деление
# except ZeroDivisionError:  # Проверка на делимость на ноль
#     print("Деление на 0!")


# PI = 3.14
# form = input("Введите форму комнаты(треугольник, прямоугольник и круг): ")
# if form == "треугольник":
#     a = int(input("Введите длину стороны1: "))
#     b = int(input("Введите длину стороны2: "))
#     c = int(input("Введите длину стороны3: "))
#     p = (a + b + c) / 2
#     s = sqrt(p * (p - a) * (p - b) * (p - c))
#     print(s)
# elif form == "прямоугольник":
#     a = int(input("Введите длину стороны1: "))
#     b = int(input("Введите длину стороны2: "))
#     s = a * b  # Нахождение площади прямоугольника
#     print(s)
# elif form == "круг":
#     r = int(input("Введите радиус круга: "))
#     s = PI * (r ** 2)  # Нахождение площади круга с глобальной переменной и возведением в степень
#     print(s)


# number1 = int(input("Введите число: "))
# number2 = int(input("Введите число: "))
# number3 = int(input("Введите число: "))
# numbers = [number1, number2, number3]
# numbers.sort()  # Сортировка списка от меньшего к большему
# print(numbers[2])
# print(numbers[0])  # Принт самого маленького числа в списке
# print(numbers[1])


# number = input("Введите номер билета: ")
# numbers = []
# s1 = 0
# s2 = 0
#
# for item in number:  # Прогоняем строку number для элементов
#     numbers.append(item)  # Добавляем элемент в список numbers
#
# for item in numbers[0:3]:  # Прогоняем 3 элемента в списке
#     s1 = s1 + int(item)
#
# for item in numbers[3:6]:
#     s2 = s2 + int(item)
#
# if s1 == s2:  # Проверка на равность двух сумм
#     print("Счастливый")
# else:
#     print("Обычный")

# number = None
# summa = 0
# while number != 0:
#     number = int(input("Введите целое число: "))
#     summa = summa + number
# print(summa)


# while True:
#     number = int(input("Введите число: "))
#     if number < 10:
#         continue  # Переход на новую итарацию цикла
#     elif number > 100:
#         break
#     else:
#         print(number)


# a = int(input("Введите число №1: "))
# b = int(input("Введите число №2: "))
# c = []
# s = 0
# for i in range(a, b + 1):
#     if i % 3 == 0:  # Проверка на кратность числа нацело на 3
#         c.append(i)
# for i in c:
#     s = s + i
# print(s / len(c))


# suma = 0
# pow_finally = 0
# while True:
#     number = int(input("Введите число: "))
#     suma = suma + number
#     pow_finally = pow_finally + pow(number, 2)
#     if suma == 0:
#         break
# print(pow_finally)


# number = float(input("Введите x для функции: "))
#
#
# def function(x):
#     if x <= -2:
#         y = 1 - (x + 2) ** 2
#         return y
#     elif -2 < x <= 2:
#         y = -x / 2
#         return y
#     elif x > 2:
#         y = pow(x - 2, 2) + 1
#         return y
#
#
# print(function(number))


# try:
#     def foo(a=2, b=1):
#         print(a / b)
# except ArithmeticError:
#     print("ArithmeticError")
# except AssertionError:
#     print("AssertionError")
# except ZeroDivisionError:
#     print("ZeroDivisionError ")

# number1 = int(input("Введите число1: "))
# number2 = int(input("Введите число2: "))
#
#
# def function(x, y):
#     try:
#         delen = x / y
#         return delen
#     except ZeroDivisionError:
#         print("Деление на ноль!")
#
#
# print(function(number1, number2))


# question = input("Введите трехзначное число: ")
# def fun_num(x):
#     for i in x:
#         print(i)
#
#
# fun_num(question)


# question = input("Введите четырехзначное число: ")
#
#
# def number(x):
#     c = 0
#     for i in x:
#         c = c + int(i)
#     return c
#
#
# print(number(question))


# question1 = int(input("Введите число: "))
# question2 = int(input("Введите число: "))
# question3 = int(input("Введите число: "))
# all_numbers = [question1, question2, question3]
# print(max(all_numbers))


# def num_check():
#     x = int(input("Введите число: "))
#     a = int(input("Введите число: "))
#     b = int(input("Введите число: "))
#     if a <= x <= b or a >= x >= b:
#         return True
#     else:
#         return False
#
#
# print(num_check())


# def null_funct():
#     numbers = []
#     while True:
#         number = int(input("Введите число: "))
#         if number == 0:
#             break
#         else:
#             numbers.append(number)
#     return len(numbers)
#
#
# print(null_funct())


# def null_funct():
#     c = 0
#     while True:
#         number = int(input("Введите число: "))
#         if number == 0:
#             break
#         else:
#             c = c + number
#     return c
#
#
# print(null_funct())


# def null_funct():
#     numbers = []
#     n = int(input("Введите число n: "))
#     while True:
#         number = int(input("Введите число: "))
#         if number == 0:
#             break
#         else:
#             numbers.append(number)
#     if n in numbers:
#         return numbers.count(n)
#     else:
#         return 0
#
#
# print(null_funct())


def null_funct():
    numbers = []
    while True:
        number = int(input("Введите число: "))
        if number == 0:
            break
        else:
            numbers.append(number)
    return numbers.count(max(numbers))


print(null_funct())