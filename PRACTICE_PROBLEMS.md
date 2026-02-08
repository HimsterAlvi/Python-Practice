# 10 Practice Problems — Learn by Solving

**How to use:** Run `python learn_by_solving.py` from this folder. Then:
- Type **1** through **10** to show that problem (description, example, hint).
- Create your solution in `solution_1.py`, `solution_2.py`, … (or any filename).
- Type **r 2** to run your solution for problem 2 (uses sample input).
- Type **t 2** to run automated tests for problem 2.
- Type **c 2** to run code_checker on your solution and get improvement tips.
- Type **q** to quit. Log what you learned in CODING_REFERENCE.md.

---

## Problem 1: Positive or Negative (if/else)
**Topic:** `if` / `else`  
**Difficulty:** ★☆☆

Ask the user for a number. Print `"Positive"` if it's greater than 0, `"Negative"` if it's less than 0, and `"Zero"` if it's 0.

**Example:** Input `-5` → Output `Negative`  
**Hint:** SYNTAX_TUTORIAL.md → "if / elif / else"

---

## Problem 2: Sum 1 to N (for loop)
**Topic:** `for`, `range`  
**Difficulty:** ★☆☆

Ask the user for a positive integer `n`. Compute and print the sum of integers from 1 to n (1 + 2 + … + n).

**Example:** Input `5` → Output `15`  
**Hint:** Use `for i in range(1, n + 1):` and add to a variable.

---

## Problem 3: Countdown (while loop)
**Topic:** `while`  
**Difficulty:** ★☆☆

Ask the user for a positive integer. Print a countdown from that number down to 1, then print `"Go!"`.

**Example:** Input `3` → Output `3`, `2`, `1`, `Go!`  
**Hint:** SYNTAX_TUTORIAL.md → "while loops". Decrease the variable each time.

---

## Problem 4: Valid Number (while + input validation)
**Topic:** `while`, `break`, input validation  
**Difficulty:** ★★☆

Keep asking the user for a number until they enter an integer between 1 and 10 (inclusive). Then print `"Valid: X"` where X is that number.

**Example:** User types `0`, `15`, `abc`, then `7` → Output `Valid: 7`  
**Hint:** CODING_REFERENCE.md → "Repeat until valid input". Use `while True:` and `break` only when valid. Use `str.isdigit()` or try/except for numbers.

---

## Problem 5: Multiplication Table (nested for)
**Topic:** `for`, nested loops  
**Difficulty:** ★★☆

Ask for an integer `n` (e.g. 5). Print the multiplication table for 1 through n: row i lists i×1, i×2, … i×n.

**Example:** Input `3` → Output:
```
1 2 3
2 4 6
3 6 9
```
**Hint:** Two `for` loops: outer for rows, inner for columns.

---

## Problem 6: Area of Circle (function + math)
**Topic:** functions, `return`, `math`  
**Difficulty:** ★★☆

Write a function `circle_area(radius)` that **returns** the area of a circle. Use `math.pi`. Ask the user for radius (validate: positive and &lt; 1000), call the function, then print the result.

**Example:** Input `5` → Output like `The area is 78.54...`  
**Hint:** CODING_REFERENCE.md → "Circle area", "Prefer return over print".

---

## Problem 7: List of Squares (lists + for)
**Topic:** lists, `for`  
**Difficulty:** ★★☆

Ask the user for a positive integer `n`. Build a list of the squares of numbers from 1 to n, then print the list.

**Example:** Input `4` → Output `[1, 4, 9, 16]`  
**Hint:** Start with `squares = []`, loop and `squares.append(i ** 2)`.

---

## Problem 8: Min and Max (function + list)
**Topic:** functions, lists  
**Difficulty:** ★★☆

Write a function `min_max(numbers)` that takes a list of numbers and **returns** a tuple `(smallest, largest)`. Don’t use the built-in `min`/`max`. Ask the user for 3 numbers, put them in a list, call `min_max`, then print the result.

**Example:** Input `3`, `1`, `2` → Output `(1, 3)`  
**Hint:** Loop over the list; keep track of smallest and largest so far.

---

## Problem 9: Word Repeater (function + string)
**Topic:** functions, strings  
**Difficulty:** ★★☆

Write a function `repeat_word(word, n)` that returns `word` repeated `n` times with a space between (e.g. `"hi", 3` → `"hi hi hi"`). Ask the user for a word and a number, call the function, print the result.

**Example:** Input `hello`, `2` → Output `hello hello`  
**Hint:** You can use `(word + " ") * n` and strip the trailing space, or a loop.

---

## Problem 10: Simple Counter Class (OOP)
**Topic:** class, `__init__`, methods  
**Difficulty:** ★★★

Create a class `Counter` with:
- `__init__(self, start=0)` — initial value is `start`.
- `increment(self)` — adds 1 to the counter.
- `value(self)` — returns the current value.

Create a counter starting at 0, call `increment` three times, then print the value (should be 3).

**Example:** No input; output `3`  
**Hint:** SYNTAX_TUTORIAL.md → "OOP — Classes and objects". Use `self` to store the current count.

---

## Suggested order

1 → 2 → 3 → 4 → 5 (control flow and loops)  
6 → 7 → 8 → 9 (functions and data)  
10 (OOP)

Log each solved problem in **CODING_REFERENCE.md** under "My Problems".
