# class Person:
#     pass
#
#
# tom = Person()

# class Person:
#     def say_hello(self):
#         print("hello")
#
#
# tom = Person()
# tom.say_hello()

# class Person():
#     def say(self, message):
#         print(message)
#
#
# tom = Person()
# tom.say("hello world")

# class Person():
#     def say(self, message):
#         print(message)
#
#     def say_hello(self):
#         self.say("hello world")
#
#
# tom = Person()
# tom.say_hello()

# class Person:
#     def __init__(self):
#         print("Создание объекта в Person")
#
#
# tom = Person()

# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.age = 1
#
#
# tom = Person("Tom")
# print(tom.name)
# print(tom.age)
# tom.age = 20
# print(tom.age)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_info(self):
#         print(f"name: {self.name}, age: {self.age}")
#
#
# tom = Person("Tom", 22)
# tom.display_info()
# ivan = Person("Ivan", 14)
# ivan.display_info()

class Auto:
    def __init__(self, brand, model, age):
        self.brand = brand
        self.model = model
        self.age = age

    def info_car(self):
        print(f"brand: {self.brand}, model: {self.model}, age: {self.age}")

    def info_brand(self):
        print(self.brand)

    def info_model(self):
        print(self.model)

    def info_age(self):
        print(self.age)


bmw = Auto("BMW", "X5", 2016)
bmw.info_car()
bmw.info_model()
opel = Auto("OPEL", "ASTRA", 2003)
opel.info_age()
opel.info_car()
bmw.info_age()