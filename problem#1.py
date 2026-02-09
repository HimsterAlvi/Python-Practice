"""
Name: Hammad Alvi

Problem#1:
Topic: if / else
Difficulty: ★☆☆

Ask the user for a number. Print "Positive" if it's greater than 0, "Negative" if it's less than 0, and "Zero" if it's 0.

Example: Input -5 → Output Negative
Hint: SYNTAX_TUTORIAL.md → "if / elif / else"

"""

num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
