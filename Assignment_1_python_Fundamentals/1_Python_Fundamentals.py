'''
Python Fundamentals

Exercise 1
Write Python code that prints your name, student number and email address.
An example runs of the program:
Bob
ST1001
bob@gmail.com

Exercise 2
Write Python code that prints your name, student number and email address using escape sequences.
An example runs of the program:
Bob
ST1001
bob@gmail.com

Exercise 3
Write Python code that add, subtract, multiply and divide the two numbers. You can use the two numbers 14 and 7.  An example run of the program:
14 + 7 = 21
14 * 7 = 98
14 – 7 = 7
14 / 7 = 2

Exercise 4
Write Python code that displays the numbers from 1 to 5 as steps.
An example runs of the program:
1
2
3
4
5

Exercise 5
Write Python code that outputs the following sentence (including the quotation marks and line break) to the screen:
An example runs of the program:
"SDK" stands for "Software Development Kit", whereas
"IDE" stands for "Integrated Development Environment".

Exercise 6
Practice and check the output
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")

Exercise 7
Define the variables below. Print the types of each variable. What is the sum of your variables? (Hint: use a type conversion function.) What datatype is the sum?
num=23
textnum="57"
decimal=98.3

Exercise 8
calculate the number of minutes in a year using variables for each unit of time. print a statement that describes what your code does also. Create three variables to store no of days in a year, minute in a hour, hours in a day, then calculate the total minutes in a year and print the values
(hint) total number of minutes in an year =No.of days in an year * Hours in a day * Minutes in an hour

Exercise 9
Write Python code that asks the user to enter his/her name and then output/prints his/her name with a greeting.
An example runs of the program:
Please enter you name: Tony
Hi Tony, welcome to Python programming :)

Exercise 10
Name your file: PoundsToDollars.py
Write a program that asks the user to enter an amount in pounds (£) and the program calculates and converts an amount in dollar ($)
An example runs of the program:
Please enter amount in pounds: XXX
£ XXX are $ XXX

'''
#Exercise 1
# Write Python code that prints your name, student number and email address.
# An example runs of the program:
# name = "Rashid VM"
# student_number = "DSMl_41"
# email_address = "rashbsf@gmail.com"
#
# print(name)
# print(student_number)
# print(email_address)

# Exercise 2
# Write Python code that prints your name, student number and email address using escape sequences.
# An example runs of the program:
# Bob
# ST1001
# bob@gmail.com
# name = "Rashid VM"
# student_number = "DSML_41"
# email_address = "rashbsf@gmail.com"
# print("Rashid VM \nDSML_41 \nrashbsf@gmail.com ")

# Exercise 3
# Write Python code that add, subtract, multiply and divide the two numbers. You can use the two numbers 14 and 7.  An example run of the program:
# 14 + 7 = 21
# 14 * 7 = 98
# 14 – 7 = 7
# 14 / 7 = 2
# Define the numbers
# num1 = 14
# num2 = 7

# Perform the operations
# addition = num1 + num2
# subtraction = num1 - num2
# multiplication = num1 * num2
# division = num1 / num2

# Print the results in one line
# print(f"{num1} + {num2} = {addition}\n{num1} - {num2} = {subtraction}\n"
#       f"{num1} * {num2} = {multiplication}\n{num1} / {num2} = {division}")
# what is f
# In Python, f before a string denotes an f-string, or formatted string literal.
# F-strings provide a way to embed expressions inside string literals using curly braces {}

# Exercise 4
# Write Python code that displays the numbers from 1 to 5 as steps.
# An example runs of the program:
# 1
# 2
# 3
# 4
# 5

# for i in range(1, 6):
#     print(i)

# Exercise 5
# Write Python code that outputs the following sentence (including the quotation marks and line break) to the screen:
# An example runs of the program:
# "SDK" stands for "Software Development Kit", whereas
# "IDE" stands for "Integrated Development Environment".

# print("\"SDK\" stands for \"Software Development Kit","\
#        \n\"IDE\" stands for \"Integrated Development Environment\".")

# Exercise 6
# # Practice and check the output
# print("python is an \"awesome\" language.")
# print("python\n\t2023")
# print('I\'m from Entri.\b')
# print("\65")
# print("\x65")
# print("Entri", "2023", sep="\n")
# print("Entri", "2023", sep="\b")
# print("Entri", "2023", sep="*", end="\b\b\b\b")

# Exercise 7
# Define the variables below. Print the types of each variable. What is the sum of your variables? (Hint: use a type conversion function.) What datatype is the sum?
# num=23
# textnum="57"
# decimal=98.3
# num = 23
# textnum = "57"
# decimal = 98.3

# print(type(num))
# print(type(textnum))
# print(type(decimal))

# sum_of_variables = num + int(textnum) + decimal
# print(sum_of_variables)

# print(type(sum_of_variables))  #<class 'float'>

# Exercise 8
# calculate the number of minutes in a year using variables for each unit of time. print a statement that describes what your code does also. Create three variables to store no of days in a year, minute in a hour, hours in a day, then calculate the total minutes in a year and print the values
# (hint) total number of minutes in an year =No.of days in an year * Hours in a day * Minutes in an hour

# Define the variables
# days_in_year = 365
# minutes_in_hour = 60
# hours_in_day = 24
#
# # Calculate the total minutes in a year
# total_minutes_in_year = days_in_year * hours_in_day * minutes_in_hour
#
# # Print the result
# print(total_minutes_in_year)
#
# # Exercise 9
# # Write Python code that asks the user to enter his/her name and then output/prints his/her name with a greeting.
# # An example runs of the program:
# # Please enter you name: Tony
# # Hi Tony, welcome to Python programming :)
#
# # Ask the user to enter their name
# name = input("Please enter your name: ")
#
# # Print a greeting
# print(f"Hi {name}, welcome to Python programming :)")

# Ask the user to enter their name
# name = input("Please enter your name: ")
#
# # Print a greeting
# print(f"Hi {name}, welcome to Python programming :)")

# Exercise 10
# Name your file: PoundsToDollars.py
# Write a program that asks the user to enter an amount in pounds (£) and the program calculates and converts an amount in dollar ($)
# An example runs of the program:
# Please enter amount in pounds: XXX
# £ XXX are $ XXX

# PoundsToDollars.py

# Define the conversion rate from pounds to dollars
conversion_rate = 1.30

# Ask the user to enter an amount in pounds
pounds = float(input("Please enter amount in pounds: £"))

# Convert pounds to dollars
dollars = pounds * conversion_rate

# Print the result
print(f"£{pounds} are ${dollars:.2f}")


#thank you






