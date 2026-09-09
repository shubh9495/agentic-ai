# DAY 3 — FUNCTIONS & DECORATORS
#
# Topics:
# 1. Functions
# 2. Parameters & Arguments
# 3. Return
# 4. Default Arguments
# 5. Keyword Arguments
# 6. *args
# 7. **kwargs
# 8. Scope
# 9. Lambda
# 10. Higher-Order Functions
# 11. Decorators
# 12. API / AI Usage


# 1. FUNCTIONS

# def greet():
#     print("Hello!")


# greet()


# 2. PARAMETERS & ARGUMENTS

# def greet_user(name):
#     print("Hello", name)


# greet_user("Shubham")


# 3. RETURN

# def add(a, b):
#     return a + b


# result = add(10, 20)
# print(result)


# 4. DEFAULT ARGUMENTS

# def greet(name="User"):
#     print("Hello", name)


# greet()
# greet("Shubham")


# 5. KEYWORD ARGUMENTS

# def student(name, age):
#     print(name, age)


# student(age=23, name="Shubham")


# 6. *args

# def total(*numbers):
#     print(numbers)
#     print(sum(numbers))


# total(10, 20, 30)


# 7. **kwargs

# def user_info(**data):
#     print(data)


# user_info(name="Shubham", age=23)


# 8. SCOPE

# x = 10


# def show():
#     x = 20
#     print(x)


# show()
# print(x)


# 9. LAMBDA

# square = lambda x: x * x

# print(square(5))


# 10. HIGHER-ORDER FUNCTION

# def calculate(func, x):
#     return func(x)


# print(calculate(square, 5))


# 11. DECORATOR

# def decorator(func):

#     def wrapper():
#         print("Before function")
#         func()
#         print("After function")

#     return wrapper


# @decorator
# def hello():
#     print("Hello!")


# hello()


# 12. DECORATOR WITH *args AND **kwargs

# def log(func):

#     def wrapper(*args, **kwargs):
#         print("Function called")
#         result = func(*args, **kwargs)
#         return result

#     return wrapper


# @log
# def add_numbers(a, b):
#     return a + b


# print(add_numbers(10, 20))


# PRACTICE

# 1. Create a function to find the sum of two numbers.

# 2. Create a function to check even/odd.

# 3. Use *args to find the maximum number.

# 4. Use **kwargs to print student details.

# 5. Create a lambda function for cube.

# 6. Create a higher-order function.

# 7. Create a decorator that prints "Function Started".