#     Python-Functions
#  ---------------------

#1) What does the len() function do in Python? Write a code example using len()
# to find the length of a list.
#  Answer:
#---------
#Define a list
# my_list=["welcome",1,2,3,4,5,6,7,7.5,"thankyou"]
#use the len() function to find the list length
# length_of_list=len(my_list)
# print ("the length of the list is",length_of_list)
# --------------------   ---------------   ------------
#2)  Write a Python function greet(name) that takes a person's name as input
# and prints "Hello, [name]!".
#Answer
#------
# def greet():
#     name=input("please enter your name: ")
#     print("Hello,{}!".format(name))
# #
#     #Example
# greet()
#--------------------          ---------------
# 3)Write a Python function find_maximum(numbers) that takes a list of integers
# and returns the maximum value without using the built-in max() function.
# Use a loop to iterate through the list and compare values
# Answer
#---------
# def find_maximum(number):
#     max_value=number[0]   #The first number is the maximum initially
#
#     #iterate through the list starting from the second element
#
#     for num in number[1:]:
#         if num > max_value:
#             max_value=num
#     return max_value
# #  example
#
# number=[7,1,5,8,9,3,4,2,6]
# print(number)
# max_value=find_maximum(number)
# print ("maximum value in the list is :",max_value)
#-------------------- -------   ---------------------------

# 4)Explain the difference between local and global variables in a Python function.
# Write a program where a global variable and a local variable have the same name and
# show how Python differentiates between them.
#
# Global variable
# message = "Hello from the global scope!"

# def greet():
#     # Local variable with the same name as the global variable
#     message = "Hello from the local scope!"
#     print(message)
#
# # Print the global variable
# print("Outside function:", message)
#
# Call the function and print the local variable
# greet()

# Print the global variable again to show it hasn't changed
# print("Outside function:", message)
#  ------------------ ------   -------------------  --------------

# 5) Create a function calculate_area(length, width=5) that calculates the area of a rectangle.
# If only the length is provided, the function should assume the width is 5.
# Show how the function behaves when called with and without the width argument.

#Answer
#-------
def calculate_area(length, width=5):
    return length * width
# #-------------
# #example:  (when both length and width provided)
area_with_both =calculate_area(12,9)
print("both length and width provided:",area_with_both)
#
# #example :(When only the length is provided )
length_only=calculate_area(10)
print("Area with only length provided(width defaults to 5):",length_only)
# # -------------------- ----------- --------- ----------------------------

