# class Animal:
#     def eat(self):
#         print("animal is eating")
# class Dog(Animal):
#     def bark(self):
#         print("dog is barking")
# obj = Dog()
# obj.eat()
# obj.bark()                
# class Father:
#     def house(self):
#         print("Father has house")
# class Son(Father):
#     def bike(self):
#         print("son has bike and they ride with father.")
# s = Son()
# s.house()
# # s.bike() 
#             multiple inheritance    
# class Father:
#     def saleem(self):
#         print("father of salman")
# class Mother:
#     def seema(self):
#         print("mother of salman")
# class Son(Father,Mother):
#     def salman(self):
#         print("salman is the son of seema and saleem.")
# s = Son()
# s.saleem()
# s.seema()
# s.salman()                
# multilevel inheritance
# class grandfather:
#     def house(self):
#         print("grandfather has house")
# class father(grandfather):
#     def house1(self):
#         print("grandfather give house to father.")
# class child(father):
#     def house2(self):
#         print("father give house to thier child.")                
# c =  child()
# c.house()
# c.house1()
# c.house2()
# heirarchnial inheritance
# class parent:
#     def rel(self):
#         print("parent")
# class child1(parent):
#     def rel2(self):
#         print("child1 is son father.")
# class child2(parent):
#     def rel3(self):
#         print("child2 is son of father")
# o = child1()
# j = child2()
# o.rel2()
# j.rel3()   
# super keyword
# class Animal:
#     def show(self):
#         print("animal has 4 lleg")
# class dog(Animal):
#     def show(self):
#         print("dog inherit animal class")  
#         super().show()                                   
# d = dog()
# d.show()        
# class Parent:
#     def __init__(self):
#         print("Parent constructor")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("Child constructor")

# c = Child(
# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# d = Dog()
# d.sound()
# polymorphism
# class Dog:
#     def sound(self):
#         print("dog barks")
# class Cat:
#     def sound(self):
#         print("Cat meows")
# class Lion:
#     def sound(self):
#         print("Lions Roar")            
# s = Dog()
# d = Cat()
# l = Lion()
# s.sound()
# d.sound()
# l.sound()        
# polymorphism using inheritance
# class Animal:
#     def sound(self):
#         print("Animal makes sound")
# class Dog(Animal):
#     def sound(self):
#         print("dog barks")
# class Cat:
#     def sound(self):
#         print("Cat meows")
# d = Dog()
# c = Cat()
# d.sound()
# c.sound()                        
# class Teacher:
#     def work(self):
#         print("Teacher teaches Student.")
# class Doctor:
#     def work(self):
#         print("Doctor treat patient")
# def Profession(person):
#     person.work()

# t = Teacher()
# d = Doctor()
# Profession(t)
# Profession(d)             
# encapsulation
# class Animal:
#     def __show(self):
#          print("animal")
# a = Animal()
# a.__show()
# class Bank:
#     def __init__(self):
#         self.__balance = 1000
#     def show_balance(self):
#         print(self.__balance)    
# d  =  Bank()
# d.show_balance()        