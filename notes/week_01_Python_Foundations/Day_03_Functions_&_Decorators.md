# Day 3 — Python Functions & Decorators

## Topics Covered

1. **Functions** — Creating reusable blocks of code
2. **Parameters & Arguments** — Passing data into functions
3. **Return Statement** — Returning results from functions
4. **Default Arguments** — Providing default values for parameters
5. **Keyword Arguments** — Passing arguments using parameter names
6. **`*args`** — Passing a variable number of positional arguments
7. **`**kwargs`** — Passing a variable number of keyword arguments
8. **Scope** — Understanding local and global variables
9. **Lambda Functions** — Creating small anonymous functions
10. **Higher-Order Functions** — Passing and returning functions
11. **Decorators** — Adding functionality to existing functions
12. **Practical Usage** — Functions and decorators in APIs, automation, and Agentic AI

---

# 1. Functions

A **function** is a reusable block of code that performs a specific task.

Instead of writing the same code again and again, we put it inside a function and call the function whenever we need it.

### Basic Idea

```text
Create function
      ↓
Write the task
      ↓
Call the function
      ↓
Task gets executed
```

Functions are useful because they make code:

* Reusable
* Easier to understand
* Easier to maintain
* Less repetitive

---

# 2. Parameters & Arguments

Functions can receive data from outside.

### Parameter

A **parameter** is the variable written when defining a function.

```text
def greet(name):
```

Here, `name` is a parameter.

### Argument

An **argument** is the actual value passed when calling the function.

```text
greet("Shubham")
```

Here, `"Shubham"` is the argument.

### Easy Way to Remember

```text
Parameter → variable in function definition

Argument  → actual value during function call
```

A function can also have multiple parameters.

---

# 3. Return Statement

The `return` statement sends a value back from a function.

For example:

```text
function
   ↓
does some work
   ↓
return result
   ↓
caller receives result
```

### `print()` vs `return`

These are different.

**`print()`**

Displays something on the screen.

**`return`**

Sends a value back to the code that called the function.

A returned value can be:

* Stored in a variable
* Used in another calculation
* Passed to another function
* Used inside a condition

This makes `return` very important when building reusable functions.

---

# 4. Default Arguments

A **default argument** gives a parameter a value that will be used when the caller does not provide one.

For example, a function can have:

```text
name = "User"
```

as its default value.

If no name is provided, `"User"` is used.

If a value is provided, that value replaces the default.

### Idea

```text
No argument
     ↓
Use default value
```

```text
Argument provided
     ↓
Use provided value
```

Default arguments are useful when a function has a common or optional value.

---

# 5. Keyword Arguments

Arguments can be passed using the **parameter name**.

Instead of depending only on the position of the argument, we explicitly tell Python which parameter gets which value.

For example:

```text
student(name="Shubham", age=23)
```

The parameter names make the function call easier to understand.

### Advantage

When using keyword arguments, the order does not have to match the parameter order.

For example:

```text
student(age=23, name="Shubham")
```

is also valid.

---

# 6. `*args`

`*args` allows a function to accept a **variable number of positional arguments**.

Normally, a function may expect a fixed number of arguments.

With `*args`, we can pass any number of positional values.

For example:

```text
add_numbers(10, 20)

add_numbers(10, 20, 30, 40)
```

Both calls can work with the same function.

### Inside the Function

Inside the function, `args` behaves like a **tuple**.

Conceptually:

```text
*args
  ↓
tuple of positional arguments
```

This makes `*args` useful when we don't know beforehand how many positional values the function will receive.

---

# 7. `**kwargs`

`**kwargs` allows a function to accept a **variable number of keyword arguments**.

For example:

```text
name="Shubham"
age=23
city="Dehradun"
```

can all be passed to the same function.

### Inside the Function

`kwargs` behaves like a **dictionary**.

Conceptually:

```text
**kwargs
    ↓
dictionary
    ↓
key → value
```

Because it is a dictionary, we can use dictionary methods such as `items()` and loop through the data.

### `*args` vs `**kwargs`

| Feature         | `*args`              | `**kwargs`        |
| --------------- | -------------------- | ----------------- |
| Accepts         | Positional arguments | Keyword arguments |
| Inside function | Tuple                | Dictionary        |
| Example         | `10, 20, 30`         | `name="Shubham"`  |

---

# 8. Scope

**Scope** determines where a variable can be accessed in a program.

The two basic scopes covered here are:

* Local scope
* Global scope

---

## Local Variable

A variable created inside a function is normally local to that function.

It can be used inside that function but cannot normally be accessed from outside it.

Think:

```text
Function
┌─────────────────┐
│ local variable  │
└─────────────────┘
```

The variable belongs to that function.

---

## Global Variable

A variable created outside a function has global scope.

A function can access a global variable when it is available in the surrounding scope.

---

## `global` Keyword

The `global` keyword can be used when a function needs to **modify a global variable**.

Without `global`, assigning to a variable inside a function normally creates a local variable instead.

### Important

Global variables should not be used unnecessarily.

It is usually easier to maintain functions when they:

```text
receive data → parameters
process data
return result → return
```

rather than depending heavily on global state.

---

# 9. Lambda Functions

A **lambda function** is a small anonymous function.

Anonymous means that the function does not need to be created using a normal `def` function definition.

### Syntax

```text
lambda arguments: expression
```

For example:

```text
lambda x: x * x
```

means:

```text
Take x
   ↓
multiply x by x
   ↓
return result
```

Lambda functions are useful for **small and simple operations**.

They are commonly seen with functions such as `map()`.

### When Not to Use Lambda

If the logic becomes complicated, a normal `def` function is usually easier to read and understand.

---

# 10. Higher-Order Functions

A **higher-order function** is a function that does at least one of these:

1. Takes another function as an argument
2. Returns another function

Python allows functions to be treated like values.

That means a function can be:

* Stored in a variable
* Passed to another function
* Returned from another function

---

## Passing a Function as an Argument

A function can be passed to another function.

Concept:

```text
function A
    ↓
passed to
    ↓
function B
    ↓
function B executes A
```

This is useful when we want one function to control **when or how another function is executed**.

---

## Returning a Function

A function can also create and return another function.

This is especially important for understanding **decorators**.

---

# 11. Decorators

A **decorator** is a function that adds or modifies functionality of another function **without changing the original function's code**.

This is one of the most important concepts from Day 3.

### Real-World Idea

Imagine you have a basic function:

```text
Do task
```

Now you want to add:

```text
Log before task
Do task
Log after task
```

Instead of changing the original function, a decorator can wrap it.

```text
          Decorator
              ↓
      ┌───────────────┐
      │ Before        │
      │               │
      │ Original      │
      │ Function      │
      │               │
      │ After         │
      └───────────────┘
```

The original function remains focused on its actual job.

The decorator handles the additional behavior.

---

## How a Decorator Works

A basic decorator usually contains:

1. A decorator function
2. A wrapper function
3. The original function
4. A call to the original function inside the wrapper
5. The wrapper being returned

Conceptually:

```text
decorator(func)
      ↓
   wrapper()
      ↓
extra functionality
      ↓
func()
      ↓
more functionality
```

---

## `@decorator` Syntax

Python provides a convenient syntax:

```text
@decorator
def greet():
    ...
```

This is essentially equivalent to:

```text
greet = decorator(greet)
```

The decorator takes the original function and replaces it with the wrapped version.

---

## Decorators with Arguments

A decorator may need to work with functions that receive different arguments.

For this reason, the wrapper commonly uses:

```text
*args
**kwargs
```

This allows the wrapper to accept a flexible number of positional and keyword arguments.

The wrapper can then pass those arguments to the original function.

---

## Returning the Original Result

If the original function returns a value, the wrapper should generally return that value as well.

Conceptually:

```text
result = func(...)
return result
```

Otherwise, the returned value could be lost.

---

## Common Uses of Decorators

Decorators are commonly used for cross-cutting functionality such as:

* Logging
* Authentication
* Timing functions
* Validation
* Access control
* API endpoints

This is why decorators become especially useful in frameworks such as FastAPI and other Python applications.

---

# 12. Practical Usage in APIs and Agentic AI

Functions are everywhere in real Python applications.

For example, an API might have a function responsible for getting a user.

An AI application might have a function responsible for generating an LLM response.

A RAG application might have a function responsible for retrieving relevant documents.

This gives applications a clean structure:

```text
API
 ↓
function

LLM
 ↓
function

RAG retrieval
 ↓
function

Tool
 ↓
function
```

---

## Functions in Agentic AI

Agentic AI systems are built from many individual operations.

For example:

```text
User Query
    ↓
Retrieve Documents
    ↓
Call Tool
    ↓
Process Result
    ↓
Generate Response
```

Each step can be implemented as a separate function.

This makes the system easier to:

* Understand
* Test
* Debug
* Reuse
* Extend

---

## Decorators in APIs and AI

Decorators can add functionality around existing functions.

For example, a decorator can:

```text
Before function
    ↓
Log request
    ↓
Run function
    ↓
Log result
```

The original function does not need to contain the logging code itself.

This separation becomes useful in:

* API development
* Authentication
* Logging
* Monitoring
* Validation
* Agent workflows

---

# Quick Revision

| Concept               | Simple Meaning                              |
| --------------------- | ------------------------------------------- |
| Function              | Reusable block of code                      |
| Parameter             | Variable defined by a function              |
| Argument              | Actual value passed to a function           |
| `return`              | Sends a value back                          |
| Default Argument      | Provides a default value                    |
| Keyword Argument      | Passes value using parameter name           |
| `*args`               | Variable positional arguments               |
| `**kwargs`            | Variable keyword arguments                  |
| Scope                 | Determines where a variable can be accessed |
| Lambda                | Small anonymous function                    |
| Higher-Order Function | Takes or returns another function           |
| Decorator             | Adds functionality around a function        |

---