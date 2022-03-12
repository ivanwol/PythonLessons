# string = input("Введите число: ")
# if string.isnumeric(): # Возвращает True если строка написана цифрами
#     a = int(string)
#     print(a)
#     print(type(a))
# else:
#     print(string)
#     print(type(string))

# file_name = "task.txt"
# start = file_name.startswith("lesson") |
#                                         Проверка строки на наличие куска с конца или с начала строки
# end = file_name.endswith(".py")        |
# print(end)

# string = "   hello  world!  "
# finall = string.strip()  # Убирает пробелы с краев строки
# print(string)
# print(finall)

# print("Madrid", "5000000".rjust(10))  # Делает 10 мини-пробелов между двумя элементами

# welcome = "Hello world! Goodbye world!"
# index1 = welcome.find("wor")  # Поиск заданной части в строке и принт ее индекса
# print(index1)

# index2 = welcome.find("wor", 10)  # Поиск заданной части в строке после заданного индекса
# print(index2)
#
# print(welcome[3:20])
# index3 = welcome.find("wor", 3, 20)  # Поиск заданной части в строке в определенном промежутке
# print(index3)

# phone = "+1-234-567-89-10"
# edited_phone = phone.replace("-", "")  # Замена символов в строке на другие символы
# print(phone)
# print(edited_phone)

# edited_phone = phone.replace("-", "", 2)  # Замена символов в строке на другие символы некоторое количество раз
# print(phone)
# print(edited_phone)

# phone = "380-98-96!40 695"
# phone1 = phone.replace("-", "")
# phone2 = phone1.replace("!", "")
# phone3 = phone2.replace(" ", "")
# print(phone3)

# text = "Это был огромный, в два обхвата дуб, с обломанными ветвями и с обломанной корой"
# print(text)
# splitted_text = text.split()  # Разделение строки по словам
# print(splitted_text)
# splitted_text2 = text.split(",")  # Разделение строки по запятым
# print(splitted_text2)
# splitted_text3 = text.split(" ", 5)  # Разделение строки по пробелу до определеного момета
# print(splitted_text3)

# words = ["Let", "me", "speak", "from", "my", "heart", "in", "English"]
# print(words)
# sentence = " ".join(words)  # Объединение элементов списка в строку с разделителем пробел!
# print(sentence)
# sentence2 = "!".join(words)
# print(sentence2)