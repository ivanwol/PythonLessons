# class Person:
#     def __init__(self, name):  # Создание конструктора, который принимает name
#         self.__name = name  # Создание атрибута класса
#
#     @property  # Описание аннотации gettera
#     def name(self):  # Создание метода name
#         return self.__name  # Возвращение приватного атрибута
#
#     def display_info(self):  # Создание метода display_info
#         print(f"name: {self.__name}")
#
#
# class Employee:
#     def __init__(self, name):  # Создание конструктора, который принимает name
#         self.__name = name  # Создание атрибута класса
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f"name: {self.__name}")
#
#     def work(self):  # Создание метода work
#         return f"{self.__name} works"
#
# class Person:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f"name: {self.__name}")
#
#
# class Employee(Person):  # Создание дочерного класса
#     def work(self):  # Создание метода work
#         print(f"{self.name} works")
#
#
# tom = Employee("Tom")  # Создание объекта класса
# print(tom.name)
# tom.display_info()
# tom.work()

# class Employee:
#     def work(self):  # Создание метода work
#         print("Employee works")
#
#
# class Student:
#     def study(self):  # Создание метода study
#         print("Студент учится")
#
#
# class WorkingStudent(Employee, Student):  # Создание дочерного класса
#     pass
#
#
# tom = WorkingStudent()
# tom.work()
# tom.study()


# class Country:
#     def __init__(self, name):  # Создание конструктора, который принимает name
#         self.__name = name  # Создание атрибута класса
#
#     @property  # Описание аннотации gettera
#     def name(self):  # Создание метода name
#         return self.__name
#
#     def display_info(self):  # Создание метода display_info
#         print(f"country name: {self.__name}")
#
#
# class City:
#     def __init__(self, name):  # Создание конструктора, который принимает name
#         self.__name = name  # Создание атрибута класса
#
#     @property  # Описание аннотации gettera
#     def name(self):  # Создание метода name
#         return self.__name  # Возврат приватного атрибута
#
#     def info(self):  # Создание метода info
#         print(f"city name: {self.name}")
#
#
# class CountryCity(Country, City):  # Создание дочерного класса
#     pass
#
#
# italy = CountryCity("Italy")
# italy.display_info()
# italy.info()