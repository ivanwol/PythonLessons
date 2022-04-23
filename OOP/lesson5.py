# class Person:
#     type = "Person"
#     descriptionPerson = "Good friend"
#
#
# print(Person.type)
# print(Person.descriptionPerson)
# Person.type = "2 person"
# print(Person.type)


# class Person:
#     type = "Person"
#
#     def __init__(self, name):
#         self.name = name
#
#
# obj1 = Person("Ivan")
# obj2 = Person("Serhii")
# print(obj1.type)
# print(obj2.type)
#
# Person.type = "person 2"
# print(obj1.type)
# print(obj2.type)


# class Person:
#     default_name = "None"
#
#     def __init__(self, name):
#         if name:
#             self.name = name
#         else:
#             self.name = Person.default_name
#
#
# obj1 = Person("Ivan")
# obj2 = Person("")
# print(obj1.name)
# print(obj2.name)


# class Person:
#     name = "None"
#
#     def print_name(self):
#         print(self.name)
#
#
# obj1 = Person()
# obj2 = Person()
# obj1.print_name()
# obj2.print_name()
#
# obj1.name = "Egor"
# obj1.print_name()
# obj2.print_name()
#
# Person.name = "info"
# obj1.print_name()
# obj2.print_name()


class Person:
    __type = "Person"

    @staticmethod
    def print_type():
        print(Person.__type)


Person.print_type()

obj1 = Person()
obj1.print_type()