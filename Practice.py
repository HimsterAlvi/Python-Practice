# 1)Write a Python program that calculates the area of a circle based on the radius entered by the user.
# import math

# def circle_area (radius):
#     area = 3.14* pow(radius,2)
#     print ("the area of the circle is "+str(area))

# radius = float(input("Enter the circle radius "))

# while radius > 0:
#     if radius > 0 and radius < 100:
#         circle_area(radius)
#     else:
#         print("please enter a radius in the range of 0 to 100")
#     break

# 2) Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java

# def file_name_func ():
#     extension_index = file_name.find(".")
#     extension = file_name[extension_index:]
#     print ("the file extension is "+extension)

# file_name = input("enter a file name with the entension ")

# file_name_func()

# OR
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print("The extension of the file is : " + repr(f_extns[-1]))
