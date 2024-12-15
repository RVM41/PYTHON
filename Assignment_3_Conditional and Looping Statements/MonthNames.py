  # 3_Conditional and Looping Statements
#--------------------  ------  -------------
# Exercise 1
#-----------
#  Integer value from the user
# month = int(input("Enter the month (1-12): "))

#month names
# months = ["January", "February", "March", "April", "May", "June",
#           "July", "August", "September", "October", "November", "December"]

# if 1 <= month <= 12:
#     print(f"Month {month} is {months[month - 1]}")
# else: print("Invalid month. Please enter a number between 1 and 12.")
#---------------------      -----------------------    ----------------------------
# Exercise 2, Cinema Ticket Pricing
#-------------      --------------
# age = int(input("Enter your age: "))
# # Ticket pricing logic
# if age < 16:
#     price = 6 * 0.5
# elif age >= 60:
#     price = 6 / 3
# else: price = 6
# print(f"Your ticket costs £{price:.2f}")
# -----------  --------- --------- -------------------
# Exercise 3
# ----------
# BodyMassIndex.py

# Read weight and height from the user
# weight = float(input("Enter your weight in (kg): "))
# height = float(input("Enter your height in (m): "))

#  Exercise 3 ,Calculate BMI
# bmi = weight / (height ** 2)

# Determine weight status
# if bmi < 18.5:
#     status = "underweight"
# elif 18.5 <= bmi < 24.9:
#     status = "normal"
# elif 25 <= bmi < 29.9:
#     status = "overweight"
# else:
#     status = "obese"
#
# print(f"Your BMI is: {bmi:.2f}")
# print(f"You are in the \"{status}\" range.")

# ----------- ------  --------------------    ------

# Exercise 4 ,GreatestNumber.py
# ------------     ------------
# Read three numbers from the user
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))
#
# # Determine the greatest number
# greatest = max(num1, num2, num3)
#
# print(f"The greatest number is: {greatest}")

# ------------------      --------------------


#   Exercise 5 ,Factorial.py
# -- ------ ------ ---------

# Read a number from the user
# num = int(input("Enter a number: "))
#
# # Initialize factorial
# factorial = 1
#
# # Calculate factorial using a loop
# for i in range(1, num + 1):
#     factorial *= i
#
# print(f"The factorial of {num} is: {factorial}")
#  ------------ ---------  -------------  -----------------

# Exercise 6 ,ReverseNumber.py
# ----------------------------

# Read a number from the user
# num = int(input("Enter a number: "))

# Initialize reversed number
# reversed_num = 0

# Reverse the number using while loop
# while num > 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10
#
# print(f"The reversed number is: {reversed_num}")

# -------------------------------------------------------
# Exercise 7 ,Multiples.py
# -------------------------

# Read a number from the user
# num = int(input("Enter a number: "))
#
# # Find multiples of the number
# print(f"Multiples of {num}:")
# for i in range(1, 11):
#     print(num * i)

# ------------- ------- -----------------
# Exercise 8
# PrintAndBreak.py
# -----------------
# while True:
#     value = input(":")
#     if value == 'done':
#         print("Done")
#         break
#     else:
#         print(value)





#  Exercise 9,FizzBuzz.py
#    ------------------

#
# for i in range(1, 11):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# ----------------------------------------------------

# Exercise 10 Pattern.py


for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

#     ------------------------ ---------------- ---------------









