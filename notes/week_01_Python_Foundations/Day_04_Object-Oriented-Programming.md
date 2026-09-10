# Day 4 — Object-Oriented Programming (OOP)

OOP is a programming approach where we organize code using classes and objects.
It helps us write code that is reusable, organized, and easier to maintain.

## Topics Covered

1. **Classes & Objects** — Creating classes and objects
2. **Attributes & Methods** — Defining data and behavior
3. **`__init__` Constructor** — Initializing objects
4. **`self`** — Referring to the current object
5. **Encapsulation** — Controlling access to data
6. **Inheritance** — Reusing and extending classes
7. **Polymorphism** — Using the same method with different behavior
8. **Abstraction** — Hiding unnecessary implementation details
9. **Class vs Instance Variables** — Understanding shared and object-specific data
10. **Magic/Dunder Methods** — Understanding methods like `__str__()` and `__len__()`
11. **Composition** — Building classes using other classes
12. **Practical Usage** — Using OOP in APIs and AI applications

## 1. Classes and Objects

A class is a blueprint for creating objects.

An object is an instance of a class.

```python
class Car:
    pass

car1 = Car()
car2 = Car()
```

Here:

* `Car` is the class.
* `car1` and `car2` are objects.

One class can be used to create many objects.

## 2. Attributes and Methods

Attributes store data.

Methods define behavior.

```python
class Car:

    def start(self):
        print("Car started")


car = Car()
car.start()
```

Here:

* `Car` → class
* `car` → object
* `start()` → method

## 3. `__init__()` Constructor

`__init__()` runs automatically when an object is created.

It is used to initialize object data.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Shubham", 25)

print(student.name)
print(student.age)
```

Output:

```text
Shubham
25
```

When we write:

```python
student = Student("Shubham", 25)
```

Python automatically calls `__init__()`.

## 4. `self`

`self` refers to the current object.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Now:

```python
student1 = Student("Rahul")
student2 = Student("Aman")

print(student1.name)
print(student2.name)
```

Output:

```text
Rahul
Aman
```

`self.name` stores the name separately for each object.

## 5. Encapsulation

Encapsulation means keeping data and the methods that work with that data together.

Python uses `__` to indicate internal/private attributes.

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

print(account.get_balance())
```

Output:

```text
5000
```

The balance is accessed through a method instead of directly.

## 6. Inheritance

Inheritance allows one class to reuse another class.

```python
class Vehicle:

    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    pass


car = Car()
car.start()
```

Output:

```text
Vehicle started
```

`Car` inherits the `start()` method from `Vehicle`.

Relationship:

```text
Vehicle
   ↓
  Car
```

## 7. Polymorphism

Polymorphism means the same method can behave differently for different objects.

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

Output:

```text
Bark
Meow
```

Both classes have `sound()`, but the behavior is different.

## 8. Abstraction

Abstraction means hiding unnecessary implementation details and exposing only what is needed.

For example, when using an ATM, we only interact with:

```text
Enter PIN
Select amount
Withdraw money
```

We do not need to know how the banking system works internally.

Python can implement abstraction using abstract classes.

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):

    def pay(self):
        print("Payment through UPI")
```

The `Payment` class defines what must be implemented, while `UPI` provides the actual implementation.

## 9. Class and Instance Variables

### Instance Variable

An instance variable belongs to a specific object.

```python
class Student:

    def __init__(self, name):
        self.name = name


student1 = Student("Rahul")
student2 = Student("Aman")
```

Here:

```text
student1.name → Rahul
student2.name → Aman
```

Each object has its own `name`.

### Class Variable

A class variable is shared by objects.

```python
class Student:

    college = "GEHU"

    def __init__(self, name):
        self.name = name
```

Both objects can access:

```python
student1.college
student2.college
```

Result:

```text
GEHU
GEHU
```

## 10. Magic / Dunder Methods

Dunder methods have double underscores.

Examples:

```python
__init__
__str__
__len__
```

`__str__()` controls how an object is represented as a string.

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


student = Student("Shubham")

print(student)
```

Output:

```text
Shubham
```

## 11. Composition

Composition means one class contains an object of another class.

For example, a car has an engine.

```python
class Engine:

    def start(self):
        print("Engine started")


class Car:

    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car started")


car = Car()
car.start()
```

Output:

```text
Engine started
Car started
```

Here, `Car` contains an `Engine` object.

This is called a "has-a" relationship.

Inheritance is usually an "is-a" relationship.

```text
Car is a Vehicle
Car has an Engine
```

## 12. OOP in AI Applications

OOP is commonly used in larger Python applications.

For example:

```python
class Agent:

    def __init__(self, name):
        self.name = name

    def run(self, question):
        print(f"{self.name} is processing: {question}")


agent = Agent("Support Agent")

agent.run("Where is my order?")
```

Output:

```text
Support Agent is processing: Where is my order?
```

In an Agentic AI project, we can have classes such as:

```text
Agent
LLM
Tool
Memory
RAG
VectorStore
APIClient
```

This keeps a large application organized and reusable.

## Quick Revision

| Concept       | Meaning                            |
| ------------- | ---------------------------------- |
| Class         | Blueprint                          |
| Object        | Instance of a class                |
| Attribute     | Data stored in an object           |
| Method        | Function inside a class            |
| `__init__()`  | Initializes an object              |
| `self`        | Refers to the current object       |
| Encapsulation | Keeps data and behavior together   |
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

By the end of Day 4, you should understand:

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

OOP will become useful when building larger projects such as FastAPI applications, RAG systems, and Agentic AI applications.
