# Day 4 — Object-Oriented Programming (OOP)

OOP is a programming approach where code is organized using **classes and objects**.

It helps make code reusable, organized, and easier to maintain.

## Topics Covered

1. **Classes & Objects**
2. **Attributes & Methods**
3. **`__init__()` Constructor**
4. **`self`**
5. **Encapsulation**
6. **Inheritance**
7. **Polymorphism**
8. **Abstraction**
9. **Class & Instance Variables**
10. **Magic / Dunder Methods**
11. **Composition**
12. **OOP in AI Applications**

## 1. Classes & Objects

### Class

A class is a blueprint for creating objects.

### Object

An object is an instance of a class.

One class can create multiple objects.

## 2. Attributes & Methods

### Attribute

Stores data inside an object.

Example:

```text
name
age
price
```

### Method

A function defined inside a class.

It defines the behavior of an object.

## 3. `__init__()` Constructor

`__init__()` runs automatically when an object is created.

It is mainly used to initialize object data.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

When we create:

```python
student = Student("Shubham")
```

Python automatically calls `__init__()`.

## 4. `self`

`self` refers to the current object.

```python
self.name
self.age
```

Each object gets its own values.

```text
student1.name → Rahul
student2.name → Aman
```

`self` is required as the first parameter of an instance method.

## 5. Encapsulation

Encapsulation means keeping data and the methods that work with that data together.

Python commonly uses:

```text
_name      → protected/internal convention
__name     → private/name-mangled convention
```

Example:

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance
```

The balance can be accessed through a method instead of directly.

## 6. Inheritance

Inheritance allows one class to reuse and extend another class.

```text
Vehicle
   ↓
  Car
```

Example relationship:

```text
Car is a Vehicle
```

The child class can use methods from the parent class.

## 7. Polymorphism

Polymorphism means the same method can have different behavior for different objects.

Example:

```text
Dog.sound() → Bark
Cat.sound() → Meow
```

Both classes have the same method name:

```text
sound()
```

But the behavior is different.

## 8. Abstraction

Abstraction means hiding unnecessary implementation details and exposing only what is needed.

Example: ATM

```text
Enter PIN
Select amount
Withdraw money
```

You use the ATM without knowing how the banking system works internally.

Python provides abstraction using **abstract classes** and the `abc` module.

### Encapsulation vs Abstraction

| Concept       | Meaning                        |
| ------------- | ------------------------------ |
| Encapsulation | Protect/control access to data |
| Abstraction   | Hide implementation details    |

## 9. Class & Instance Variables

### Instance Variable

Belongs to a specific object.

Usually created using `self`.

```python
self.name = name
```

Example:

```text
student1.name → Rahul
student2.name → Aman
```

Each object has its own value.

### Class Variable

Belongs to the class and is shared by objects.

```python
class Student:
    college = "GEHU"
```

Both objects can access:

```text
student1.college
student2.college
```

## 10. Magic / Dunder Methods

Dunder methods are special methods whose names start and end with `__`.

Examples:

```text
__init__()
__str__()
__len__()
__add__()
__eq__()
__lt__()
__repr__()
```

They allow objects to work with Python's built-in operations.

### Common Dunder Methods

| Method       | Purpose                           |
| ------------ | --------------------------------- |
| `__init__()` | Initialize an object              |
| `__str__()`  | Define output for `print()`       |
| `__len__()`  | Define behavior of `len()`        |
| `__add__()`  | Define behavior of `+`            |
| `__eq__()`   | Define behavior of `==`           |
| `__lt__()`   | Define behavior of `<`            |
| `__repr__()` | Developer-friendly representation |

## 11. Composition

Composition means one class contains an object of another class.

### Inheritance

**IS-A relationship**

```text
Car is a Vehicle
```

### Composition

**HAS-A relationship**

```text
Car has an Engine
```

Composition is useful when one object uses or contains another object.

## 12. OOP in AI Applications

OOP is useful for organizing larger AI applications.

An Agentic AI project can have classes such as:

```text
Agent
LLM
Tool
Memory
RAG
VectorStore
APIClient
```

Each class can handle a specific responsibility.

This makes large applications easier to organize, reuse, and maintain.

## Quick Revision

| Concept       | Meaning                            |
| ------------- | ---------------------------------- |
| Class         | Blueprint                          |
| Object        | Instance of a class                |
| Attribute     | Data stored in an object           |
| Method        | Function inside a class            |
| `__init__()`  | Initializes an object              |
| `self`        | Refers to current object           |
| Encapsulation | Controls access to data            |
| Inheritance   | Reuses another class               |
| Polymorphism  | Same method, different behavior    |
| Abstraction   | Hides implementation details       |
| Composition   | One class contains another object  |
| Dunder Method | Special method such as `__str__()` |

## Practice

1. Create a `Car` class with:

   * `brand`
   * `model`
   * `price`
   * `show_details()`

2. Create a `BankAccount` class with:

   * `deposit()`
   * `withdraw()`
   * `get_balance()`

3. Create an `Animal` class and inherit it into a `Dog` class.

4. Create `Dog` and `Cat` classes with a common `sound()` method.

5. Create an `Agent` class with:

   * `name`
   * `model`
   * `run()`

## Day 4 Goal

Understand:

```text
Class
  ↓
Object
  ↓
Attributes + Methods
  ↓
__init__ + self
  ↓
Encapsulation
  ↓
Inheritance
  ↓
Polymorphism
  ↓
Abstraction
  ↓
Composition
  ↓
OOP in real applications
```