"""
Name: Hammad Alvi
Problem#3:
Topic: while loop
Difficulty: ★☆☆

Ask the user for a positive integer. Print a countdown from that number down to 1, 
then print "Go!"

Example: Input 3 → Output 3, 2, 1, Go!
Hint: while loop; decrease variable each time

"""

num = int(input("Enter a positive integer: "))
if num <= 0:
    print("Please enter a positive integer")
    exit()
    
while num > 0:
    print(num)
    num -= 1

print("Go!")