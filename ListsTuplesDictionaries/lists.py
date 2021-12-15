# numbers = [1, 2, 3, 4, 5]  # Создание листа и наполнение его елементами
# print(numbers)


# numbers1 = []  # Создание пустого листа
# numbers2 = list([1, 2, 3])
# Создание пустого листа №2
# print(numbers2)


# numbers = [1, 2, 3, 4, 5]  # Создание листа и наполнение его елементами от 1 до 5
# numbers2 = numbers  # Создание листа и присвоение елементов другова листа
# numbers3 = list(numbers)  # Создание листа и присвоение елементов другова листа
# print(numbers)
# print(numbers2)
# print(numbers3)


# numbers = [1, 2, 3, 4, 5]
# print(numbers[-3])  # Принт значения елемента с индексом -3
# numbers[2] = "Ivan"  # Замена елемента с индексом -2 на елемент "Ivan"
# print(numbers)


# numbers = [1, 2.6, "Hello", True, False, []]  # Создание листа со всеми типами данных которые мы знаем
# print(numbers)
# print(numbers[-1])  # Принт значения елемента с индексом -1
# numbers[2] = "Good bye"  # Замена елемента с индексом 2 на елемент "Good bye"
# print(numbers)


# numbers = [5] * 6  # Увеличивает количество елементов в листе
# print(numbers)


# numbers = [range(10)]  # Создание листа и присвоение ему функции range
# numbers2 = list(range(10))  # Создание листа и присвоение чисел от 0 до 9
# print(numbers)
# print(numbers2)
# numbers3 = list(range(5, 10))  # Создание листа и присвоение чисел от 5 до 9
# print(numbers3)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Создание листа и присвоение ему чисел от 1 до 9
# numbers2 = list(range(1, 100))  # Создание листа и присвоение ему чисел от 1 до 99
# print(numbers)
# print(numbers2)


# objects = [1, 2.4, True, "Hello", [1, 2, 3]]  # Создание листа со всеми типами данных которые мы знаем
# for i in objects:  # Перебор елементов циклом for
#     print(i)
#
# objects2 = [1, 2.4, True, "Hello", [1, 2, 3]]  # Создание листа со всеми типами данных которые мы знаем
# i = 0  # Создание счеткика елементов
# while i < len(objects2):  # Перебор елементов циклом while
#     print(objects2[i])
#     i = i + 1  # Увеличение счетчика


# numbers = [1, 2, 3, 4, 5]
#
#
# def alt_past_list(x):  # Создание функции которая принимает параметры функции list
#     for i in x:  # Создание цикла который прогоняет елеиенты списка
#         print(i)
#
#
# alt_past_list(numbers)  # Вызов функции


# numbers = [1, 2, 3, 4, 5]
#
#
# def past_list(x):  # Создание функции которая принимает параметры функции list
#     numbers2 = []  # Создание пустого листа
#     for i in x: # Создание цикла который прогоняет елеиенты списка
#         numbers2.append(i)  # Добавление елементов в новый список
#     return numbers2
#
#
# print(past_list(numbers))


# numbers = [6, 1, 8, 4, 2, 3, 4, 0,  5, 5, 5, 5, -1, -1, -5, 6]
# # numbers.append("Ivan")  # Добавление элемента в конец списка
# print(numbers)
# # print(numbers.index("Ivan"))  # Ищем индекс элемента
# print(numbers.count(5))  # Частота повторения элемента в списке
# numbers.sort()  # Сортировка элементов в списке от меньшео до большего
# print(numbers)
# numbers.reverse()  # Оборачивает список началом в конец
# print(numbers)
# users = ["Serhii", "Ivan", "Ana"]
# users.insert(2, "Victor")  # Добавление элемента в список по индексу
# print(users)
# numbers = [6, -7, 8, 3, 1.5, 1, 2, 3, 4, 5]
# print(len(numbers))  # Подсчет количества элементов в списке
# print(sorted(numbers))  # Сортировка элементов в списке от меньшео до большего
# print(min(numbers))  # Принт минимального значения списка
# print(max(numbers))  # Принт максимального значения списка


