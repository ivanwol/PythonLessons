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


