# class Person:
#     last_name = ""
#     def __init__(self, name):
#         self.name = name
# p1 = Person("Alice")
# p2 = Person("Bob")
# p1.last_name = "refsnes"
# p2.last_name = "refsnes"
# print(p1.last_name)
# print(p2.last_name)


# from unicodedata import name


# class Person: 
#     def __init__(self, name): 
#         self.name = name 
# p1 = Person("Tobias") 
# p1.age = 25 
# p1.city = "Oslo" 
# print(p1.name) 
# print(p1.age) 
# print(p1.city)


# 
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def greet(self):
#         print("Hello, my name is " + self.name)
# p1 = Person("Alice")
# p1.greet()
# class calculator:
#     def add(self, a, b):
#         return a + b
#     def subtract(self, a, b):
#         return a - b
#     def multiply(self, a, b):
#         return a * b
#     def divide(self, a, b):
#         if b != 0:
#             return a / b
#         else:
#             return "Cannot divide by zero"
# calc = calculator()
# print(calc.add(10, 5))
# print(calc.subtract(10, 5))
# print(calc.multiply(10, 5))
# print(calc.divide(10, 5))
# print(calc.divide(10, 0))
# class rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2 * (self.width + self.height)
# r1 = rectangle(5, 3)
# print("Area:", r1.area())
# print("Perimeter:", r1.perimeter())
# try:
#     li = [1]*(10**10)
# except MemoryError as e:
#     print(e)
# p = open(r'C:\Users\dell\OneDrive\Desktop\coding\python\mymodule.py')
# print(p.read())
r = open("superman.txt",'a')
r.write("hello i hello.")
r.close()
print(r)