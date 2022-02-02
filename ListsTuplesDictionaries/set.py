# users = {"Ivan", "Serhii", "Egor", "Ivan"}
# print(users)


# users = ["Ivan", "Ivan", "Egor", "Ana", "Ana"]
# print(users)
# users_set = set(users)
# print(users_set)


# users = set()
# print(users)
# users2 = {}
# print(users2)


# car = {"Mercedes", "BMW", "Toyota"}
# print(len(car))


# cars = set()
# cars.add("Toyota")
# print(cars)


# users = {"Serhii", "Ivan", "Viktor", "Yana"}
# del_user = input("Введите пользователя которого хотите удалить: ")
# if del_user in users:
#     users.remove(del_user)
# print(users)


# users = {"Serhii", "Ivan", "Viktor", "Yana"}
# print(users)
# del_user = input("Введите пользователя которого хотите удалить: ")
# users.discard(del_user)
# print(users)


# users = {"Serhii", "Ivan", "Viktor", "Yana"}
# users.clear()
# print(users)


# users = {"Serhii", "Ivan", "Viktor", "Yana"}
# for i in users:
#     print(i)


# users = {"Serhii", "Ivan", "Viktor", "Yana"}
# users2 = users.copy()
# print(users)
# print(users2)


# users = {"Serhii", "Ivan", "Viktor", "Yana"}
# users2 = {"Egor", "Katerina", "Fedor"}
# users3 = users.union(users2)
# print(users)
# print(users2)
# print(users3)


# users = {"Serhii", "Ivan", "Viktor", "Yana"}
# users2 = {"Egor", "Katerina", "Viktor"}
# users3 = users.intersection(users2)
# print(users3)


# users = {"Serhii", "Ivan", "Viktor", "Yana"}
# users2 = {"Egor", "Katerina", "Viktor"}
# users3 = users2.difference(users)
# print(users3)


# def countries():
#     country = []
#     while True:
#         question = input("Введите страну: ")
#         if question != "Stop":
#             country.append(question)
#         else:
#             break
#     country_set = set(country)
#     return country_set
#
#
# print(countries())