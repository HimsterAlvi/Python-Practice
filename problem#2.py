"""
Name: Hammad Alvi

Problem#2:
Topic: for, range
Difficulty: ★☆☆

## Problem 2: Sum 1 to N (for loop)
**Topic:** `for`, `range`
**Difficulty:** ★☆☆

Ask the user for a positive integer `n`.
Compute and print the sum of integers from 1 to n (1 + 2 + … + n).

**Example:** Input `5` → Output `15`
**Hint:** Use `for i in range(1, n + 1):` and add to a variable.
"""

n = int(input("Enter a positive integer: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print(sum)
