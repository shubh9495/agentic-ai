# DAY 4 — OBJECT-ORIENTED PROGRAMMING
#
# Topics:
# 1. Classes & Objects
# 2. Attributes & Methods
# 3. __init__()
# 4. self
# 5. Encapsulation
# 6. Inheritance
# 7. Polymorphism
# 8. Abstraction
# 9. Class & Instance Variables
# 10. Dunder Methods
# 11. Composition
# 12. OOP in AI


# ==================================================
# 1. CLASS & OBJECT
# ==================================================

# class Car:
#     pass
#
#
# car1 = Car()
# car2 = Car()


# ==================================================
# 2. ATTRIBUTES & METHODS
# ==================================================

# class Car:
#
#     def __init__(self, brand):
#         self.brand = brand
#
#     def start(self):
#         print("Car started")
#
#
# car = Car("BMW")
#
# print(car.brand)
# car.start()


# ==================================================
# 3. __init__()
# ==================================================

# class Student:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# student = Student("Shubham", 25)
#
# print(student.name)
# print(student.age)


# ==================================================
# 4. self
# ==================================================

# class Student:
#
#     def __init__(self, name):
#         self.name = name
#
#
# student1 = Student("Rahul")
# student2 = Student("Aman")
#
# print(student1.name)
# print(student2.name)


# ==================================================
# 5. ENCAPSULATION
# ==================================================

# class BankAccount:
#
#     def __init__(self, balance):
#         self.__balance = balance
#
#     def get_balance(self):
#         return self.__balance
#
#
# account = BankAccount(5000)
#
# print(account.get_balance())


# ==================================================
# 6. INHERITANCE
# ==================================================

# class Vehicle:
#
#     def start(self):
#         print("Vehicle started")
#
#
# class Car(Vehicle):
#     pass
#
#
# car = Car()
#
# car.start()


# ==================================================
# 7. POLYMORPHISM
# ==================================================

# class Dog:
#
#     def sound(self):
#         print("Bark")
#
#
# class Cat:
#
#     def sound(self):
#         print("Meow")
#
#
# dog = Dog()
# cat = Cat()
#
# dog.sound()
# cat.sound()


# ==================================================
# 8. ABSTRACTION
# ==================================================

# from abc import ABC, abstractmethod
#
#
# class Payment(ABC):
#
#     @abstractmethod
#     def pay(self):
#         pass
#
#
# class UPI(Payment):
#
#     def pay(self):
#         print("Payment through UPI")
#
#
# payment = UPI()
#
# payment.pay()


# ==================================================
# 9. INSTANCE VARIABLE
# ==================================================

# class Student:
#
#     def __init__(self, name):
#         self.name = name
#
#
# student1 = Student("Rahul")
# student2 = Student("Aman")
#
# print(student1.name)
# print(student2.name)


# ==================================================
# CLASS VARIABLE
# ==================================================

# class Student:
#
#     college = "GEHU"
#
#     def __init__(self, name):
#         self.name = name
#
#
# student1 = Student("Rahul")
# student2 = Student("Aman")
#
# print(student1.college)
# print(student2.college)


# ==================================================
# 10. DUNDER METHODS
# ==================================================

# __str__()

# class Student:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#
# student = Student("Shubham")
#
# print(student)


# __len__()

# class Team:
#
#     def __init__(self, members):
#         self.members = members
#
#     def __len__(self):
#         return len(self.members)
#
#
# team = Team(["A", "B", "C"])
#
# print(len(team))


# __add__()

# class Number:
#
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         return self.value + other.value
#
#
# a = Number(10)
# b = Number(20)
#
# print(a + b)


# ==================================================
# 11. COMPOSITION
# ==================================================

# class Engine:
#
#     def start(self):
#         print("Engine started")
#
#
# class Car:
#
#     def __init__(self):
#         self.engine = Engine()
#
#     def start(self):
#         self.engine.start()
#         print("Car started")
#
#
# car = Car()
#
# car.start()


# ==================================================
# 12. OOP IN AI
# ==================================================

# class Agent:
#
#     def __init__(self, name, model):
#         self.name = name
#         self.model = model
#
#     def run(self, question):
#         print(f"{self.name} is processing: {question}")
#
#
# agent = Agent("Support Agent", "Gemini")
#
# agent.run("Where is my order?")


# ==================================================
# PRACTICE
# ==================================================

# 1. Create a Car class.
#    - brand
#    - model
#    - price
#    - show_details()

# 2. Create a BankAccount class.
#    - deposit()
#    - withdraw()
#    - get_balance()

# 3. Create Animal and inherit Dog from it.

# 4. Create Dog and Cat with sound().

# 5. Create an Agent class.
#    - name
#    - model
#    - run()