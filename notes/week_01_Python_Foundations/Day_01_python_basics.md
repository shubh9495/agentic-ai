# This 7-day Python foundation is designed to build the core programming skills required for Agentic AI development.



# Day 1 — Python Core

## Overview

Python Core covers the fundamental concepts required to start programming in Python.
In this day, we focus on variables, data types, strings, type conversion, input/output, operators, and conditional statements.

 

# 1. Variables

A **variable** is a name used to store a value in memory.

Python is a **dynamically typed language**. This means we do not need to explicitly declare the data type of a variable.

For example, unlike C/C++, we don't need to write the type before creating a variable.

Python determines the type automatically from the assigned value.

### Dynamic Typing

A variable can refer to different types of values during program execution.

 text
x → integer
x → string
 

This is allowed because Python is dynamically typed.

### Multiple Variable Assignment

Python allows assigning multiple variables in a single line.

 text
name, age, city = Shubham, 25, Dehradun
 

### Same Value to Multiple Variables

The same value can also be assigned to multiple variables.

 text
a = b = c = 24
 

 

## Variable Naming Rules

Python variables must follow certain rules.

* Letters, numbers, and underscores `_` are allowed.
* A variable cannot start with a number.
* Spaces are not allowed.
* Hyphens `-` are not allowed.
* Python keywords cannot be used as variable names.
* Variable names are case-sensitive.

* ### Python Keywords

    Keywords are reserved words that have a special meaning in Python.

    Examples:

     text
    class
    def
    return
    import
    True
    False
    None
    if
    else
    for
    while
     

    Therefore, they cannot be used as normal variable names.

* ### Case Sensitivity

    Python is case-sensitive.

    These are different identifiers:

     text
    name
    Name
    NAME
     

     

# 2. Data Types

A **data type** defines what kind of value a variable contains and what operations can be performed on that value.

Python provides several built-in data types.

| Data Type  | Description         | Example    |
|    - |       - |    - |
| `int`      | Whole numbers       | `23`       |
| `float`    | Decimal numbers     | `99.5`     |
| `str`      | Text                | `"Python"` |
| `bool`     | Boolean value       | `True`     |
| `NoneType` | Represents no value | `None`     |

### Integer — `int`

Used for whole numbers.

Examples:

 text
10
25
-5
 

### Float — `float`

Used for decimal numbers.

Examples:

 text
10.5
99.99
-2.5
 

### String — `str`

Used to represent text.

Examples:

 text
"Hello"
"Python"
"Shubham"
 

### Boolean — `bool`

Represents one of two values:

 text
True
False
 

Booleans are commonly used in conditions.

### NoneType

`None` represents the absence of a value.

 text
None
 

It is commonly used when a variable currently has no meaningful value.

 

# 3. Strings

A **string** is a sequence of characters.

Strings are commonly written using:

* Single quotes `'...'`
* Double quotes `"..."`
* Triple quotes `"""..."""`

Example:

 text
"Hello"
'Python'
 

 

## String Indexing

Python uses **zero-based indexing**.

This means the first character has index `0`.

For example:

 text
Python
012345
 

So:

* `P` → index `0`
* `y` → index `1`
* `t` → index `2`
* `h` → index `3`
* `o` → index `4`
* `n` → index `5`

 

## Negative Indexing

Python also supports negative indexing.

Negative indexing starts from the end of the string.

 text
Python
-6 -5 -4 -3 -2 -1
 

Therefore:

* `-1` → last character
* `-2` → second-last character

 

## String Slicing

Slicing is used to extract a portion of a string.

### Syntax

 text
string[start:end]
 

The `start` index is included, but the `end` index is excluded.

For example:

 text
Python
012345
 

A slice from index `0` to `3` gives:

 text
Pyt
 

because index `3` is not included.

### Common Slicing Patterns

 text
string[:end]
string[start:]
string[:]
 

 

## Common String Methods

Python provides many built-in methods for working with strings.

Some commonly used methods are:

| Method         | Purpose                         |
|     -- |           - |
| `upper()`      | Converts text to uppercase      |
| `lower()`      | Converts text to lowercase      |
| `capitalize()` | Capitalizes the first character |
| `replace()`    | Replaces part of a string       |

 

## String Length

The `len()` function returns the number of characters in a string.

For example, the word:

 text
Python
 

contains `6` characters.

 

# 4. Type Conversion

**Type conversion** means changing a value from one data type to another.

Python provides several built-in functions for type conversion.

| Function  | Converts To |
|     |    -- |
| `int()`   | Integer     |
| `float()` | Float       |
| `str()`   | String      |
| `bool()`  | Boolean     |

### Common Conversions

 text
String → Integer
Integer → String
Integer → Float
Float → Integer
 

### Float to Integer

When converting a float to an integer using `int()`, Python removes the decimal portion.

It does **not** round the number.

For example:

 text
10.8 → 10
 

 

# 5. Input / Output

Input and output allow a program to communicate with the user.

 

## Output

Python uses the `print()` function to display information on the screen.

It can display:

* Text
* Numbers
* Variables
* Multiple values

 

## Input

Python uses the `input()` function to take input from the user.

### Important

`input()` **always returns a string**.

Even if the user enters a number, Python initially treats the input as a string.

Therefore, numerical input usually needs type conversion.

For example:

 text
User enters → 23
Python receives → "23"
 

To perform mathematical operations, convert it to an integer.

 

## f-Strings

An **f-string** is a convenient way to insert variables inside a string.

It is written by placing `f` before the string.

Variables can then be placed inside `{}`.

Example concept:

 text
f"Hello {name}"
 

f-strings are commonly used for readable formatted output.

 

# 6. Operators

**Operators** are symbols or keywords used to perform operations on values.

Python provides different categories of operators.

 

## Arithmetic Operators

Arithmetic operators are used for mathematical operations.

| Operator | Meaning        |
|   -- |     -- |
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |
| `//`     | Floor Division |
| `%`      | Modulus        |
| `**`     | Power          |

### Important Operators

#### `/` Division

Returns the division result.

#### `//` Floor Division

Returns the floor value of the division result.

#### `%` Modulus

Returns the remainder.

#### `**` Power

Used for exponentiation.

 

# Comparison Operators

Comparison operators compare two values.

The result is always a Boolean:

 text
True
False
 

| Operator | Meaning                  |
|   -- |          |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

 

# Logical Operators

Logical operators are used to combine or modify conditions.

## `and`

Returns `True` only when **both conditions are true**.

## `or`

Returns `True` when **at least one condition is true**.

## `not`

Reverses the Boolean result.

 text
True → False
False → True
 

 

# Assignment Operators

Assignment operators are used to assign or update values.

| Operator | Meaning             |
|   -- |       - |
| `=`      | Assign              |
| `+=`     | Add and assign      |
| `-=`     | Subtract and assign |
| `*=`     | Multiply and assign |
| `/=`     | Divide and assign   |
| `%=`     | Modulus and assign  |

These operators provide a shorter way to update variables.

 

# 7. Conditional Statements

Conditional statements allow a program to **make decisions** based on conditions.

Python provides:

* `if`
* `elif`
* `else`

 

## `if`

The `if` statement executes a block of code when its condition is `True`.

Concept:

 text
if condition:
    execute code
 

 

## `if / else`

Used when there are two possible outcomes.

Concept:

 text
if condition:
    execute if true
else:
    execute if false
 

 

## `if / elif / else`

Used when there are multiple conditions.

* `if` checks the first condition.
* `elif` checks additional conditions.
* `else` executes when none of the previous conditions are true.

Python checks the conditions from top to bottom.

Once a condition is satisfied, its block is executed.

 

# Indentation

**Indentation is very important in Python.**

Unlike languages such as C/C++, Python uses indentation to define code blocks.

Example structure:

 text
if condition:
    code inside block
 

The indented code belongs to the `if` block.

Incorrect indentation can result in an error.

 


<!-- Day 2	Collections + Loops	
Day 3	Functions + Decorators	
Day 4	OOP	
Day 5	Type Hints + Pydantic	
Day 6	JSON + APIs + Error Handling	
Day 7	Project + Revision -->