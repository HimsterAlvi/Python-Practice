# Python Syntax — Quick Tutorial

Basic syntax for **if**, **for**, **while**, and **OOP**. Use this when you forget the structure of a construct.

---

## 1. `if` / `elif` / `else`

```python
# Single condition
if x > 0:
    print("positive")

# if / else
if age >= 18:
    print("adult")
else:
    print("minor")

# if / elif / else (multiple branches)
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# Nested if
if x > 0:
    if x < 100:
        print("in range")
```

**Rules:** Colon `:` after the condition. Indent the body (4 spaces). No parentheses around the condition unless you need them for logic.

---

## 2. `for` loops

```python
# Loop over a range of numbers (0 to 4)
for i in range(5):
    print(i)   # 0, 1, 2, 3, 4

# range(start, stop) — start included, stop excluded
for i in range(2, 6):
    print(i)   # 2, 3, 4, 5

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)   # 0, 2, 4, 6, 8

# Loop over a list
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print(f)

# Loop with index: enumerate()
for index, value in enumerate(fruits):
    print(index, value)   # 0 apple, 1 banana, 2 cherry

# Loop over a string (each character)
for char in "hello":
    print(char)
```

---

## 3. `while` loops

```python
# Repeat until condition is False
count = 0
while count < 5:
    print(count)
    count += 1

# "Infinite" loop with break (e.g. valid input)
while True:
    n = input("Enter a number 1–10: ")
    if n.isdigit():
        n = int(n)
        if 1 <= n <= 10:
            break
    print("Invalid. Try again.")
print("You entered", n)
```

**Important:** Make sure the condition eventually becomes False (or you `break`), or the loop never stops.

---

## 4. Loop control: `break` and `continue`

```python
# break — exit the loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)   # 0, 1, 2, 3, 4

# continue — skip to next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)   # 0, 1, 3, 4
```

---

## 5. Functions

```python
# Define
def greet(name):
    return "Hello, " + name

# Call
msg = greet("World")
print(msg)

# With default argument
def greet(name, punctuation="!"):
    return "Hello, " + name + punctuation

# With type hints (optional)
def area(radius: float) -> float:
    return 3.14159 * radius ** 2
```

---

## 6. OOP — Classes and objects

```python
# Define a class
class Dog:
    # Constructor: runs when you create a new Dog
    def __init__(self, name, age):
        self.name = name   # instance attribute
        self.age = age

    # Instance method (first argument is always self)
    def bark(self):
        print(self.name + " says woof!")

    def describe(self):
        return f"{self.name} is {self.age} years old"

# Create objects
dog1 = Dog("Max", 3)
dog2 = Dog("Bella", 2)

# Use methods and attributes
dog1.bark()           # Max says woof!
print(dog1.name)      # Max
print(dog2.describe())  # Bella is 2 years old
```

### Key OOP ideas

| Term | Meaning |
|------|--------|
| **Class** | Blueprint (e.g. `Dog`) |
| **Object / Instance** | One concrete thing (e.g. `dog1`) |
| **`__init__(self, ...)`** | Constructor; sets up the object |
| **`self`** | The current instance inside methods |
| **Attribute** | Data on the object (`self.name`) |
| **Method** | Function defined on the class, takes `self` |

### Inheritance (optional)

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some sound")

class Cat(Animal):
    def speak(self):   # Override
        print(self.name + " says meow")

c = Cat("Whiskers")
c.speak()   # Whiskers says meow
```

---

## 7. Useful built-ins and operators

| Syntax | Purpose |
|--------|--------|
| `len(x)` | Length of string, list, etc. |
| `str(x)`, `int(x)`, `float(x)` | Type conversion |
| `x in y` | True if x is in y (string, list, etc.) |
| `x ** 2` | x squared |
| `x += 1` | Same as `x = x + 1` |
| `f"text {var}"` | F-string: embed variables in strings |

---

*Keep this file open when writing practice code. For full rules and your problem log, see `CODING_REFERENCE.md`.*
