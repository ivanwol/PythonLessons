# class Person:  # Создание класса Person
#     def __init__(self, name):  # Создание конструктора который принимает name
#         self.__name = name  # Создание приватного атрибута
#         self.__age = 1  # Создание приватного атрибута с значением по умолчанию
#
#     def set_age(self, age):  # Создание метода set_age которая принимает age
#         if 1 < age < 100:  # Проверка реалистичности возраста
#             self.__age = age  # Создание приватного атрибута
#         else:
#             print("Некоректно указан возраст")
#
#     def get_age(self):  # Создание метода get_age
#         return self.__age  # Возвращение приватного атрибута
#
#     def get_name(self):  # Создание метода get_age
#         return self.__name  # Возвращение приватного атрибута
#
#     def display_info(self):  # Создание метода display_info
#         print(f"name: {self.__name}, age: {self.__age}")  # Вывод с помощью ф строки
#
#
# tom = Person("Tom")  # Создание объекта класса
# tom.display_info()  # Обращение к методу класса
# tom.set_age(60)  # Обращение к методу set_age с указыванием и проверкой возраста
# tom.display_info()  # Обращение к методу класса

class Person:  # Создание класса Person
    def __init__(self, name):  # Создание конструктора который приниает name
        self.__name = name  # Создание приватного атрибута
        self.__age = 1  # Создание приватного атрибута с значением по умолчанию

    @property  # Создание аннотации getter
    def age(self):  # Создание метода геттера
        return self.__age  # Возвращение приватного атрибута

    @age.setter  # Создание аннотации setter с ссылкой на age
    def age(self, age):  # Создание метода age который принимает age
        if 1 < age < 100:  # Проверка на реалистичность возвраста
            self.__age = age  # Создание приватного атрибута
        else:
            print("Возраст указан некоректно")

    @property  # Создание аннотации getter
    def name(self):  # Создание метода name
        return self.__name  # Возвращение приватного атрибута

    def display_info(self):  # Создание метода display_info
        print(f"name: {self.__name}, age: {self.__age}")  # Вывод с помощью ф строки


tom = Person("Tom")
tom.display_info()
tom.age = 60
print(tom.age)
tom.display_info()