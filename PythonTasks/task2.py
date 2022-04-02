# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i < 5:
#         print(i)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# result = list(set(a) & set(b))
# print(result)

# dict_a = {1:10, 2:20}
# dict_b = {3:30, 4:40}
# dict_c = {5:50, 6:60}
# dict_d = {}
# for i in dict_a, dict_b, dict_c:
#     dict_d.update(i)
# print(dict_d)

# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# result = sorted(my_dict, key=my_dict.get, reverse=True)[0:3]
# print(result)
# word = input("Введите слово: ")


# def check(x):
#     letters = []
#     for i in x:
#         letters.append(i)
#     letters.reverse()
#     str_letters = "".join(letters)
#     if x == str_letters:
#         return True
#     else:
#         return False
#
#
# print(check(word))

# a = ["a", "b", "b", "a"]
# str = "".join(a)
# print(str)


# def check(string):
#     return string == "".join(reversed(string))
#
#
# print(check(word))


# def check(string):
#     return string == string[::-1]
#
#
# print(check(word))
# number = int(input("Введите количество секунд: "))
#
# def convert(seconds):
#     days = seconds // (24 * 3600)
#     seconds %= 24 * 3600
#     hours = seconds // 3600
#     seconds %= 3600
#     minutes = seconds // 60
#     seconds %= 60
#     print(f"{days}:дней, {hours}:часов, {minutes}:минут, {seconds}: секунд")
#
#
# convert(number)
# n = int(input("Введите целое число: "))
#
#
# def solve(n):
#     nn = n * 10 + n
#     nnn = n * 100 + nn
#     sum = n + nn + nnn
#     return sum
#
#
# print(solve(n))


# lst = [1, 2, 3, 4, 5]
# first = lst[0]
# last = lst[-1]
# print(first, last)

# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162,
#            758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217]
#
#
# def number(x):
#     for i in x:
#         if i == 237:
#             break
#         elif i % 2 == 0:
#             print(i)
#
#
# number(numbers)

# def lists(lst1, lst2):
#     return set(lst1) - set(lst2)
#
#
# print(lists(['White', 'Black', 'Red'], ['Red', 'Green']))

# lst = [1, 2, 3, 4, 5]
# a = sum(lst)
# print(a)

# def sum_digits(num):
#     u = 0
#     for i in str(num):
#         u = u + int(i)
#     return u
#
#
# print(sum_digits(5245))

# def sum_digits(num):
#     digits = []
#     for i in num:
#         digits.append(int(i))
#     return sum(digits)
#
#
# print(sum_digits("5245"))

# string = 'Python Software Foundation'
# result = string.count("O")
# print(result)

# x = 5
# y = 10
# i = [x, y]
# x = i[1]
# y = i[0]
# print(x, y)

# x = 5
# y = 10
# i = x
# x = y
# y = i
# print(x, y)

# x = 5
# y = 10
# x, y = y, x
# print(x, y)


# def numbers(x):
#     for i in x:
#         if i % 15 == 0:
#             print(i)
#
#
# numbers([45, 55, 60, 37, 100, 105, 220])


# def all_unique(numbers):
#     if len(set(numbers)) == len(numbers):
#         return True
#     else:
#         return False
#
#
# print(all_unique([45, 55, 60, 37, 100, 105, 220, 45]))

# def all_unique(numbers):
#     return len(set(numbers)) == len(numbers)
#
#
# print(all_unique([45, 55, 60, 37, 100, 105, 220]))