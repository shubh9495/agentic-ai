# 1. Variables

## Basic Variables
# name = "Shubham"
# age = 23
# salary = 40000

# print(name)
# print(age)
# print(salary)
 

# ## Dynamic Typing

# A variable can refer to different types of values.
# x = 10
# print(x)
# x = "Hello"
# print(x) 

# ## Multiple Variable Assignment

# name, age, city = "Shubham", 23, "Dehradun"
# print(name)
# print(age)
# print(city)
 
# ## Same Value to Multiple Variables

# a = b = c = 10
# print(a)
# print(b)
# print(c)
 

# # 2. Data Types

# name = "Shubham"
# age = 23
# salary = 40000
# is_working = True

# print(type(name))
# print(type(age))
# print(type(salary))
# print(type(is_working))

# Output:
# <class 'str'>
# <class 'int'>
# <class 'int'>
# <class 'bool'>
 

 

# # 3. Strings

# ## String Indexing

# name = "Python"

# print(name[0])
# print(name[1])
# print(name[5])
 

# Output:
# P
# y
# n

# ## Negative Indexing

# name = "Python"
# print(name[-1])
# print(name[-2])
 

# Output:
# n
# o
 

 

# ## String Slicing


# name = "Python"
# print(name[0:3])
 

# Output:
# Pyt
# The end index is not included.


# print(name[:3])
# print(name[2:])
# print(name[:])
 
# Output:
# Pyt
# thon
# Python
 

 

# ## String Methods
# text = "hello python"

# print(text.upper())
# print(text.lower())
# print(text.capitalize())
# print(text.replace("python", "world"))
 
# Output:
# HELLO PYTHON
# hello python
# Hello python
# hello world
 

 

# ## String Length

# name = "Shubham"
# print(len(name))
 
# Output:
# 7

# # 4. Type Conversion

# ## String → Integer
# age = "23"
# age = int(age)
# print(age)
# print(type(age))
 
# ## Integer → String
# age = 23
# age = str(age)
# print(type(age))
 

 

# ## Integer → Float
# x = 10
# x = float(x)
# print(x) 

# ## Float → Integer
# x = 10.8
# x = int(x)
# print(x)
# `int()` removes the decimal part; it does not round the number.

 

# # 5. Input / Output

# ## Print Output
# print("Hello World")
# print(10)
 
# ## Printing Multiple Values
# name = "Shubham"
# age = 23

# print(name, age)
 
# ## f-Strings
# name = "Shubham"
# age = 23

# print(f"My name is {name} and I am {age} years old.")
 
# Output:
# My name is Shubham and I am 23 years old.
 

 

# ## User Input
# name = input("Enter your name: ")
# print(name)
 

 

# ## Checking Input Type
# age = input("Enter your age: ")
# print(type(age))
# Even if the user enters:
# 23
# the type will be:
# <class 'str'>
 

 

# ## Taking Integer Input
# age = int(input("Enter your age: "))
# print(age + 1)
 

 

# # 6. Operators

# ## Arithmetic Operators
# a = 10
# b = 3

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)
 

 

# ## Comparison Operators


# a = 10
# b = 20

# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
 

# Output:


# False
# True
# False
# True
# False
# True
 

 

# ## Logical `and`
# age = 23
# has_id = True

# print(age >= 18 and has_id)
 

# Output:


# True
 

 

# ## Logical `or`


# is_student = True
# is_employee = False

# print(is_student or is_employee)

# Output:
# True
 

 

# ## Logical `not`
# is_logged_in = True
# print(not is_logged_in)
 
# Output:
# False
 

 

# ## Assignment Operators


# x = 10
# x += 5
# print(x)

# x -= 3
# print(x)

# x *= 2
# print(x)

# x /= 2
# print(x)

# x %= 3
# print(x)
 

 

# # 7. if / elif / else
# ## if
# age = 20

# if age >= 18:
#     print("You are an adult.")
 

# Output:
# You are an adult.
 

 

# ## if / else


# age = 16

# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")
 

# Output:
# Minor
 

 

# ## if / elif / else


# marks = 75

# if marks >= 90:
#     print("A")
# elif marks >= 75:
#     print("B")
# elif marks >= 60:
#     print("C")
# else:
#     print("D")
 

# Output:
# B
 

 

# # Indentation

# ## Correct
# age = 20

# if age >= 18:
#     print("Adult")
 

# ## Incorrect

# python
# age = 20

# if age >= 18:
# print("Adult")

# The second example produces an indentation error because the code inside the `if` block is not indented.

# # Mini Practice Problems

# ## 1. Personal Information

# # Take name and age as input and print: My name is Shubham and I am 23 years old.

# ## 2. Even or Odd

# # Take an integer from the user and check whether it is even or odd.


# ## 3. Positive, Negative or Zero

# # Take a number from the user and print whether it is:

# # Positive
# # Negative
# # Zero

# ## 4. Largest of Two Numbers

# # Take two numbers from the user and print the larger number.

# ## 5. Grade Calculator

# # Take marks as input and calculate the grade.

# ### Rules

# # text
# # 90+      → A
# # 75-89    → B
# # 60-74    → C
# # 40-59    → D
# # Below 40 → Fail