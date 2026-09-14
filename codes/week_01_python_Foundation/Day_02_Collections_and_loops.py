# Day 2 — Python Collections + Loops

# Practice / Coding File

# ============================================================

# 1. LISTS

# ============================================================

# Creating a list

numbers = [10, 20, 30, 40]
names = ["Shubham", "Rahul", "Aman"]

print(numbers)
print(names)

# ------------------------------------------------------------

# Accessing Elements

# ------------------------------------------------------------

names = ["Shubham", "Rahul", "Aman"]

print(names[0])
print(names[1])

# Negative indexing

print(names[-1])

# ------------------------------------------------------------

# Modifying Lists

# ------------------------------------------------------------

numbers = [10, 20, 30]

numbers[1] = 50

print(numbers)

# ------------------------------------------------------------

# Common List Methods

# ------------------------------------------------------------

numbers = [10, 20, 30]

# Add element at the end

numbers.append(40)
print(numbers)

# Add element at a specific index

numbers.insert(1, 15)
print(numbers)

# Remove a specific value

numbers.remove(20)
print(numbers)

# Remove the last element

numbers.pop()
print(numbers)

# Sort the list

numbers.sort()
print(numbers)

# Reverse the list

numbers.reverse()
print(numbers)

# Remove all elements

numbers.clear()
print(numbers)

# ------------------------------------------------------------

# List Slicing

# ------------------------------------------------------------

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])

# Start omitted

print(numbers[:3])

# End omitted

print(numbers[2:])

# Entire list

print(numbers[:])

# ============================================================

# 2. TUPLES

# ============================================================

coordinates = (10, 20)

# Accessing tuple elements

print(coordinates[0])
print(coordinates[1])

# Tuples cannot be modified

# This will produce an error:

#

# coordinates[0] = 50

# Example of fixed data

rgb = (255, 0, 0)

print(rgb)

# ============================================================

# 3. SETS

# ============================================================

# Creating a set

numbers = {1, 2, 3, 4}

print(numbers)

# ------------------------------------------------------------

# Duplicate values are automatically removed

# ------------------------------------------------------------

numbers = {1, 2, 2, 3, 3}

print(numbers)

# ------------------------------------------------------------

# Adding Elements

# ------------------------------------------------------------

numbers.add(5)

print(numbers)

# ------------------------------------------------------------

# Removing Elements

# ------------------------------------------------------------

numbers.remove(2)

print(numbers)

# ------------------------------------------------------------

# Set Operations

# ------------------------------------------------------------

a = {1, 2, 3}
b = {3, 4, 5}

# Union

print(a | b)

# Intersection

print(a & b)

# Difference

print(a - b)

# ------------------------------------------------------------

# Membership Checking

# ------------------------------------------------------------

skills = {"Python", "Java", "C++"}

print("Python" in skills)
print("JavaScript" in skills)

# ============================================================

# 4. DICTIONARIES

# ============================================================

student = {
"name": "Shubham",
"age": 23,
"course": "CSE"
}

print(student)

# ------------------------------------------------------------

# Accessing Values

# ------------------------------------------------------------

print(student["name"])
print(student["age"])

# Using get()

print(student.get("name"))

# Key does not exist → returns None

print(student.get("salary"))

# ------------------------------------------------------------

# Adding and Updating Values

# ------------------------------------------------------------

student["age"] = 24

student["city"] = "Dehradun"

print(student)

# ------------------------------------------------------------

# Removing Values

# ------------------------------------------------------------

student.pop("age")

print(student)

# ------------------------------------------------------------

# Dictionary Methods

# ------------------------------------------------------------

print(student.keys())

print(student.values())

print(student.items())

# Loop through dictionary

for key, value in student.items():
        print(key, value)

# ============================================================

# 5. FOR LOOP

# ============================================================

numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)

# ------------------------------------------------------------

# Loop Through a String

# ------------------------------------------------------------

name = "Python"

for character in name:
    print(character)

# ============================================================

# 6. WHILE LOOP

# ============================================================

count = 1

while count <= 5:
    print(count)
    count += 1

# ============================================================

# 7. BREAK

# ============================================================

for i in range(10):
    if i == 5:
        break

    print(i)

# ============================================================

# 8. CONTINUE

# ============================================================

for i in range(5):
    if i == 2:
        continue

    print(i)

# ============================================================

# 9. range()

# ============================================================

# Basic range

for i in range(5):
    print(i)

# Start and end

for i in range(1, 6):
    print(i)

# Start, end and step

for i in range(0, 10, 2):
    print(i)

# ============================================================

# 10. enumerate()

# ============================================================

names = ["Shubham", "Rahul", "Aman"]

for index, name in enumerate(names):
    print(index, name)

# ============================================================

# 11. zip()

# ============================================================

names = ["Shubham", "Rahul", "Aman"]

ages = [23, 24, 22]

for name, age in zip(names, ages):
    print(name, age)

# ============================================================

# 12. LIST COMPREHENSION

# ============================================================

numbers = [1, 2, 3, 4, 5]

# Normal approach

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)

# List comprehension

squares = [number ** 2 for number in numbers]

print(squares)

# ------------------------------------------------------------

# List Comprehension with Condition

# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)

# ============================================================

# 13. NESTED COLLECTIONS

# ============================================================

# ------------------------------------------------------------

# List of Lists

# ------------------------------------------------------------

matrix = [
[1, 2, 3],
[4, 5, 6]
]

print(matrix)

# Access row 0, column 1

print(matrix[0][1])

# ------------------------------------------------------------

# List of Dictionaries

# ------------------------------------------------------------

users = [
{"name": "Shubham", "age": 23},
{"name": "Rahul", "age": 24}
]

for user in users:
    print(user["name"])

# ============================================================

# 14. PRACTICAL API / AI STYLE DATA

# ============================================================

# ------------------------------------------------------------

# List of Messages

# ------------------------------------------------------------

messages = [
"Hello",
"Explain RAG",
"What is MCP?"
]

for message in messages:
    print(message)

# ------------------------------------------------------------

# Tool Arguments

# ------------------------------------------------------------

tool_args = {
"city": "Dehradun",
"unit": "Celsius"
}

print(tool_args["city"])
print(tool_args["unit"])

# ------------------------------------------------------------

# API-style List of Dictionaries

# ------------------------------------------------------------

documents = [
{"title": "Python", "score": 0.91},
{"title": "RAG", "score": 0.87},
{"title": "MCP", "score": 0.82}
]

for document in documents:
    print(document["title"])

# Print title and score

for document in documents:
    print(
        document["title"],
        document["score"]
    )

# ============================================================

# PRACTICE PROBLEMS

# ============================================================

# Try solving these yourself before writing the solution.

#

# 1. Find the largest number in a list.

#

# Example:

# numbers = [10, 25, 7, 40, 15]

#

# Expected:

# 40

#

#

# 2. Count how many even numbers are present in a list.

#

# Example:

# numbers = [1, 2, 4, 7, 8, 10]

#

# Expected:

# 4

#

#

# 3. Remove duplicates from a list.

#

# Example:

# numbers = [1, 2, 2, 3, 3, 4]

#

# Expected:

# [1, 2, 3, 4]

#

#

# 4. Find common elements between two lists.

#

# Example:

# a = [1, 2, 3, 4]

# b = [3, 4, 5, 6]

#

# Expected:

# 3, 4

#

#

# 5. Print each student's name and age.

#

# students = [

# {"name": "Shubham", "age": 23},

# {"name": "Rahul", "age": 24},

# {"name": "Aman", "age": 22}

# ]

#

#

# 6. Create a list containing squares of numbers from 1 to 10.

#

# Try solving it using:

# - for loop

# - list comprehension

#

#

# 7. Print only the documents having a score greater than 0.85.

#

# documents = [

# {"title": "Python", "score": 0.91},

# {"title": "RAG", "score": 0.87},

# {"title": "MCP", "score": 0.82}

# ]

#

#

# 8. Given two lists of names and ages, print them together.

#

# Use zip().

#

# names = ["Shubham", "Rahul", "Aman"]

# ages = [23, 24, 22]

#

#

# 9. Print the index and value of every item in a list.

#

# Use enumerate().

#

#

# 10. Use a while loop to print numbers from 10 down to 1.

#

# ============================================================

# END OF DAY 2

# ============================================================
