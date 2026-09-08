# Day 2 — Python Collections + Loops

## Topics Covered

1. **Lists** — Creating, accessing, modifying, and using list methods
2. **Tuples** — Working with ordered and immutable collections
3. **Sets** — Storing unique values and performing set operations
4. **Dictionaries** — Working with key-value pairs
5. **for Loops** — Iterating over collections and sequences
6. **while Loops** — Repeating code while a condition is true
7. **break & continue** — Controlling the flow of loops
8. **range()** — Generating sequences of numbers
9. **enumerate() & zip()** — Working efficiently with indexes and multiple collections
10. **List Comprehension** — Creating lists in a concise way
11. **Nested Collections** — Working with collections inside other collections
12. **Practical Usage** — Processing API and AI-related data

---

# Goal

Learn how to **store, organize, access, and process multiple values efficiently** using Python collections and loops.

---

# 1. Lists

A **list** is an ordered and mutable collection of elements.

### Ordered

Elements maintain their position, so we can access them using an index.

```text
[10, 20, 30, 40]
  0   1   2   3
```

### Mutable

Mutable means we can change the contents of a list after creating it.

Lists can contain different types of values as well.

---

## Accessing List Elements

Python uses **zero-based indexing**.

The first element has index `0`.

Negative indexing can also be used to access elements from the end.

```text
-1 → last element
-2 → second-last element
```

---

## Modifying Lists

Since lists are mutable, an existing element can be replaced using its index.

---

## Common List Methods

| Method      | Purpose                                  |
| ----------- | ---------------------------------------- |
| `append()`  | Adds an element at the end               |
| `insert()`  | Adds an element at a specific position   |
| `remove()`  | Removes a specific value                 |
| `pop()`     | Removes an element, usually the last one |
| `sort()`    | Sorts the list                           |
| `reverse()` | Reverses the list                        |
| `clear()`   | Removes all elements                     |

---

## List Slicing

Slicing extracts a portion of a list.

### Syntax

```text
list[start:end]
```

The `start` index is included, while the `end` index is excluded.

---

# 2. Tuples

A **tuple** is an ordered and **immutable** collection.

Example concept:

```text
(10, 20, 30)
```

Like lists, tuples support indexing.

### Immutable

Immutable means that once a tuple is created, its elements cannot be changed.

For example, you cannot replace one of its elements.

### When to Use Tuples

Use a tuple when the data should remain **fixed** and should not be modified.

Examples:

* Coordinates
* RGB values
* Fixed configuration values

---

# 3. Sets

A **set** is an unordered collection of **unique elements**.

The most important property of a set is that duplicates are automatically removed.

For example:

```text
{1, 2, 2, 3}
```

becomes:

```text
{1, 2, 3}
```

Because sets are unordered, you should not depend on a particular element order.

---

## Adding Elements

Use `add()` to add an element to a set.

---

## Removing Elements

Use `remove()` to remove an element.

---

## Set Operations

Sets are useful when comparing groups of unique values.

Suppose:

```text
A = {1, 2, 3}
B = {3, 4, 5}
```

### Union

Combines all unique elements from both sets.

```text
A | B
```

Result:

```text
{1, 2, 3, 4, 5}
```

### Intersection

Returns elements that exist in both sets.

```text
A & B
```

Result:

```text
{3}
```

### Difference

Returns elements that exist in the first set but not in the second.

```text
A - B
```

Result:

```text
{1, 2}
```

---

## Membership Checking

The `in` operator can be used to check whether an element exists in a set.

Sets are especially useful when you need:

* Unique values
* Fast membership checking
* Set operations

---

# 4. Dictionaries

A **dictionary** stores data as **key-value pairs**.

Think of it like a real dictionary:

```text
key → value
```

Example:

```text
name → Shubham
age → 23
course → CSE
```

Each key identifies a value.

---

## Accessing Values

Values can be accessed using their keys.

```text
dictionary["key"]
```

Another option is:

```text
dictionary.get("key")
```

### `get()` vs `[]`

Using `get()` is useful when a key might not exist.

If the requested key does not exist, `get()` returns:

```text
None
```

---

## Adding and Updating Values

Dictionaries are mutable.

You can:

* Change the value of an existing key
* Add a new key-value pair

---

## Removing Values

`pop()` can be used to remove a key-value pair.

---

## Useful Dictionary Methods

| Method     | Purpose                   |
| ---------- | ------------------------- |
| `keys()`   | Returns dictionary keys   |
| `values()` | Returns dictionary values |
| `items()`  | Returns key-value pairs   |

`items()` is especially useful when looping through a dictionary.

---

# 5. for Loop

A `for` loop is used when we want to **iterate over a collection or sequence**.

For example, if a list contains four numbers, a `for` loop can process each number one by one.

Conceptually:

```text
collection
    ↓
element 1
element 2
element 3
element 4
```

The loop runs once for each element.

---

## Looping Through Strings

Strings are also **iterable**.

That means we can process their characters one by one using a `for` loop.

---

# 6. while Loop

A `while` loop repeatedly executes code **as long as a condition is `True`**.

Conceptually:

```text
condition true?
      ↓
     YES
      ↓
run code
      ↓
check again
```

The loop stops when the condition becomes `False`.

### Important

Make sure something inside the loop eventually changes the condition.

Otherwise, the loop can continue forever, creating an **infinite loop**.

---

# 7. break and continue

These keywords control how a loop behaves.

## break

`break` immediately stops the loop.

Use it when you have found what you need or when continuing the loop is no longer necessary.

Example idea:

```text
Loop
 ↓
Condition met?
 ↓
YES → break → stop loop
```

---

## continue

`continue` skips the **current iteration** and moves to the next iteration.

The loop itself does not stop.

Example idea:

```text
Iteration
   ↓
Condition met?
   ↓
YES → skip this iteration
   ↓
Next iteration
```

### Difference

| Keyword    | What it does                     |
| ---------- | -------------------------------- |
| `break`    | Stops the entire loop            |
| `continue` | Skips only the current iteration |

---

# 8. range()

`range()` generates a sequence of numbers.

It is commonly used with `for` loops.

There are three common forms.

### `range(stop)`

Starts from `0` and goes up to, but does not include, `stop`.

```text
range(5)
→ 0, 1, 2, 3, 4
```

### `range(start, stop)`

Starts from `start` and stops before `stop`.

```text
range(1, 6)
→ 1, 2, 3, 4, 5
```

### `range(start, stop, step)`

`step` controls how much the value changes each time.

```text
range(0, 10, 2)
→ 0, 2, 4, 6, 8
```

### Important

The `stop` value is **never included**.

---

# 9. enumerate()

`enumerate()` is useful when we need both:

* The index
* The value

while looping through a collection.

Instead of manually managing an index, `enumerate()` provides it automatically.

For example:

```text
0 → Shubham
1 → Rahul
2 → Aman
```

This is cleaner than manually using:

```text
range(len(...))
```

when both index and value are required.

---

# 10. zip()

`zip()` allows us to iterate through multiple collections at the same time.

For example:

```text
names → Shubham, Rahul, Aman
ages  → 23, 24, 22
```

`zip()` pairs them:

```text
Shubham → 23
Rahul   → 24
Aman    → 22
```

This is useful when two or more collections contain related data.

---

# 11. List Comprehension

A **list comprehension** is a concise way to create a new list.

Instead of writing several lines with a loop and `append()`, we can often create the same list in one line.

### Basic Structure

```text
[expression for item in collection]
```

For example, we can create a list containing the squares of numbers.

---

## List Comprehension with Condition

A condition can also be added.

General structure:

```text
[expression for item in collection if condition]
```

This is useful for filtering data.

For example:

```text
numbers → 1, 2, 3, 4, 5, 6
```

We can create a new list containing only even numbers.

### When to Use

List comprehensions are best when the operation is:

* Simple
* Easy to understand
* A transformation or filtering operation

For complicated logic, a normal `for` loop is often more readable.

---

# 12. Nested Collections

A collection can contain another collection.

This is called a **nested collection**.

Examples:

* List inside a list
* Dictionary inside a list
* List inside a dictionary
* Dictionary inside a dictionary

---

## List of Lists

A list can contain multiple lists.

This is commonly used to represent structures such as:

* Matrices
* Tables
* Grids

Accessing data requires multiple indexes.

Concept:

```text
matrix[row][column]
```

---

## List of Dictionaries

A very common structure in real-world programming is a **list containing dictionaries**.

For example:

```text
[
    {"name": "...", "age": ...},
    {"name": "...", "age": ...}
]
```

This structure is especially common when working with API responses.

Each dictionary can represent one object or record.

---

# 13. Practical Usage in APIs and AI

Collections and loops are extremely important when working with APIs, LLMs, RAG systems, and Agentic AI.

---

## Lists in AI Applications

Lists can store things such as:

* Messages
* Documents
* Search results
* Tools
* Retrieved chunks
* Model outputs

Example concept:

```text
messages = [
    "Hello",
    "Explain RAG",
    "What is MCP?"
]
```

---

## Dictionaries in APIs

Dictionaries are commonly used to represent structured data.

They are frequently used for:

* API requests
* API responses
* JSON data
* Tool arguments
* Configuration
* Agent state

Example concept:

```text
{
    "city": "Dehradun",
    "unit": "Celsius"
}
```

---

## List of Dictionaries in API Responses

API responses frequently contain a list of objects.

For example:

```text
[
    {"title": "Python", "score": 0.91},
    {"title": "RAG", "score": 0.87},
    {"title": "MCP", "score": 0.82}
]
```

A loop can then process each object individually.

This pattern will become important when working with:

* LLM responses
* APIs
* RAG retrieval results
* Tool calls
* Agent state
* Documents
* Search results

---

# Quick Comparison

| Collection | Ordered   | Mutable | Allows Duplicates   | Main Use                    |
| ---------- | --------- | ------- | ------------------- | --------------------------- |
| List       | Yes       | Yes     | Yes                 | General collection of items |
| Tuple      | Yes       | No      | Yes                 | Fixed data                  |
| Set        | No        | Yes     | No                  | Unique values               |
| Dictionary | Key-based | Yes     | Keys must be unique | Key-value data              |

---
