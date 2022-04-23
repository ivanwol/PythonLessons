# class MoneyBox:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.counter = 0
#
#     def can_add(self, v):
#         if self.capacity >= self.counter + v:
#             return True
#         else:
#             return False
#
#     def add(self, v):
#         if self.capacity >= self.counter + v:
#             self.counter = self.counter + v
#         else:
#             return "Ошибка"
#         return self.counter
#
#
#
# x = MoneyBox(15)
# print(x.add(5))
#
# print(x.add(9))
#
# print(x.add(3))

# class Buffer:
#     def __init__(self):
#         self.current_part = []
#
#     def add(self, *a):
#         self.current_part.extend(a)
#         while len(self.current_part) - 5 >= 0:
#             print(sum(self.current_part[:5]))
#             self.current_part = self.current_part[5:]
#
#     def get_current_part(self):
#         return self.current_part
#
#
# buf = Buffer()
# buf.add(1, 2, 3)
# print(buf.get_current_part())
# buf.add(4, 5, 6)
# print(buf.get_current_part())
# buf.add(7, 8, 9, 10)
# print(buf.get_current_part())
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
# print(buf.get_current_part())

import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, x):
        super(LoggableList, self).append(x)
        self.log(x)


a = LoggableList()
a.append("msg1")
a.append("msg2")
print(a)