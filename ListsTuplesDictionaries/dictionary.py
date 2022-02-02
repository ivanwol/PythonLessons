# dictionary = {  # Создание словаря
#     "name": "Ivan",  # Добавление ключей и их значений
#     "age": 14,
#     "city": "Odessa"
# }
# print(dictionary)


# dictionary = {  # Создание словаря
#     1: "Ivan",  # Добавление ключей и их значений
#     2: "Serhii",
#     3: "Egor"
# }
# print(dictionary)


# dictionary = {
#     1: "Ivan",
#     "married": False  # Добавление в ловарь разных типов данных
# }
# print(dictionary)


# dictionary = {}  # Создание пустого словаря
# print(dictionary)
# object = dict()  # Создание пустого словаря через метод dict
# print(object)


# user_list = [
#     ["Ivan", "+380676549809"],
#     ["Serhii", "+380989640697"],
#     ["Egor", "+380778866552"]
# ]
# print(user_list)
# user_dict = dict(user_list)  # Создание словарь с помощью списка
# print(user_dict)
# print(type(user_list))
# print(type(user_dict))


# user_tuple = (
#     ("Ivan", "+380676549809"),
#     ("Serhii", "+380989640697"),
#     ("Egor", "+380778866552")
# )
# user_dict = dict(user_tuple)  # Создание словарь с помощью tuple
# print(user_tuple)
# print(user_dict)
# print(type(user_tuple))
# print(type(user_dict))


# city = {
#     "Ukraine": "Kiev",
#     "Russia": "Moscow",
#     "Italy": "Rim",
#     "Poland": "Warsaw"
# }
# print(city["Ukraine"])  # Вывод элемента с конкретным ключом
# print(city["Italy"])
# print(city["Kiev"])  # Вывод только с изпользоваем ключей


# city = {
#     "Ukraine": "Kiev",
#     "Russia": "Moscow",
#     "Italy": "Rim",
#     "Poland": "Warsaw"
# }
# print(city)
# city["Italy"] = "Kiev"  # Замена элемента с конкретным ключом
# print(city)


# question = input("Введите жанр: ")
# films = {
#     "Боевик": "Форсаж",
#     "Детектив": "Шерлок Холмс",
#     "Фантастика": "Гарри Поттер"
# }
# if question in films:  # Проверка есть ли элемент в словаре
#     print(question, "такой жанр найден")
# else:
#     print(question, "такой жанр не найден")

# question = input("Введите ключ который нужно вытащить: ")
# films = {
#     "Боевик": "Форсаж",
#     "Детектив": "Шерлок Холмс",
#     "Фантастика": "Гарри Поттер"
# }
# info = films.get(question, "такого ключа нет")  # Вытаскивает элемент или возвращает строку в случаи его отсутствия
# print(info)


# question = input("Введите ключ который хотите удалить: ")
# films = {
#     "Боевик": "Форсаж",
#     "Детектив": "Шерлок Холмс",
#     "Фантастика": "Гарри Поттер"
# }
# print(films)
# del films[question]  # Удаление пары по ключу
# print(films)


# question = input("Введите ключ который хотите удалить: ")
# films = {
#     "Боевик": "Форсаж",
#     "Детектив": "Шерлок Холмс",
#     "Фантастика": "Гарри Поттер"
# }
# if question in films:
#     film = films[question]
#     print(film)
#     del films[question]
#     print(film, "удалено")
# else:
#     print("Элемент не найден")


# question = input("Введите ключ который хотите удалить: ")
# films = {
#     "Боевик": "Форсаж",
#     "Детектив": "Шерлок Холмс",
#     "Фантастика": "Гарри Поттер"
# }
# film = films.pop(question, "элемент не найден")  # Удаление пары по ключу или вывод строки в случаи ее отсутствия
# print(films)
# print(film)


# films = {
#     "Боевик": "Форсаж",
#     "Детектив": "Шерлок Холмс",
#     "Фантастика": "Гарри Поттер"
# }
# print(films)
# films.clear()  # Полная очистка словаря
# print(films)


# films = {
#     "Боевик": "Форсаж",
#     "Детектив": "Шерлок Холмс",
#     "Фантастика": "Гарри Поттер"
# }
# films2 = films.copy()  # Полное копирование
# print(films)
# print(films2)


# films = {
#     "Боевик": "Форсаж",
#     "Детектив": "Шерлок Холмс",
#     "Фантастика": "Гарри Поттер"
# }
# films2 = {
#     "Драма": "Ромео и Джульета",
#     "Комедия": "Брилиантовая рука"
# }
# print(films)
# print(films2)
# films.update(films2)  # upgrade словаря другим
# print(films)
# print(films2)



# films = {
#     "Боевик": "Форсаж",
#     "Детектив": "Шерлок Холмс",
#     "Фантастика": "Гарри Поттер"
# }
# for i in films:
#     print(i, films[i])



# films = {
#     "Боевик": "Форсаж",
#     "Детектив": "Шерлок Холмс",
#     "Фантастика": "Гарри Поттер"
# }
# for key, value in films.items():
#     print(key, value)


# films = {
#     "Боевик": "Форсаж",
#     "Детектив": "Шерлок Холмс",
#     "Фантастика": "Гарри Поттер"
# }
# for keys in films.keys():  # Вывод ключей
#     print(keys)


# films = {
#     "Боевик": "Форсаж",
#     "Детектив": "Шерлок Холмс",
#     "Фантастика": "Гарри Поттер"
# }
# for value in films.values():  # Вывод элементов ключей
#     print(value)


users = {
    "Nikita": {
        "age": 25,
        "phone": "+380456724366",
        "email": "nikita@gmail.com"
    },
    "Dmitrii": {
        "age": 24,
        "phone": "+3803162836772",
        "email": "dmitrii@gmail.com"
    },
    "Artem": {
        "age": 32,
        "phone": "+380345678765432",
        "email": "artem@gmail.com",
        "skype": "ArtemD"
    }
}
print(users)
info = users["Nikita"]["email"]
print(info)
info1 = users["Dmitrii"]["phone"]
print(info1)
info_artem = users["Artem"]
print(info_artem)
key = "skype"
if key in  users["Artem"]:
    print(users["Artem"]["skype"])
else:
    print("skype не найден")