class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(self.__str__())

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"


obj1 = Person("Ivan", 14)
print(obj1.display_info())