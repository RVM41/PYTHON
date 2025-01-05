# Exercise 1: (score : 1)
# Write a Python program to read a file and display its contents

# file_path = "C:\\Users\\pc\\OneDrive\\Desktop\\Python_Entri\\Assignments_picture\\file _handling.txt"

# Open the file in read mode
# file1 = open(file_path, 'r')

# Read and print each line from the file
# for line in file1:
#     print(line.strip())  # strip() removes leading/trailing whitespace including newlines

# Close the file
# file1.close()

#------------------------------------------------------------------------------------------
# Exercise 2: (score : 1)
# Write a Python program to copy the contents of one file to another file
#-----Answer

# Define the paths to the source and destination files
# source_file_path = "C:\\path\\to\\source\\file.txt"
# destination_file_path = "C:\\path\\to\\destination\\file.txt"

# source_file_path = "C:\\Users\\pc\\OneDrive\\Desktop\\Python_Entri\\Assignments_picture\\file _handling.txt"
# destination_file_path ="C:\\Users\\pc\\OneDrive\\Desktop\\New folder\\python.txt"
# source_file=open(source_file_path,'r')
# destination_file=open(destination_file_path,'w')
# contents=source_file.read()
# destination_file.write(contents)
# source_file.close()
# destination_file.close()
#------------------------------------------------------------------------------------------

#Exercise 3: (score : 2)
# Write a Python program to read the content of a file and count the total number of words in that file.

#__-------Answer
# Define the path to the file
# file_path = "C:\\Users\\pc\\OneDrive\\Desktop\\New folder\\python.txt"
#
# # Initialize a variable to count the words
# word_count = 0
#
# # Open the file in read mode
# file = open(file_path, 'r')
#
# # Read the contents of the file
# contents = file.read()
#
# # Split the contents into words
# import re
# words =re.findall(r'\b\w+\b', contents)
#
# # Count the number of words
# word_count = len(words)
#
# # Close the file
# file.close()
#
# # Display the total number of words
# print(f"Total number of words: {word_count}")
#
#---------------------------------------------------------------------------------------
#Exercise 4: (score : 1)
# Write a Python program that prompts the user to input a string and converts it to an integer.
# Use try-except blocks to handle any exceptions that might occur

# Answer
#-------

user_input = input("Please enter a number: ")
try:
    # Try to convert the input to an integer
    number = int(user_input)
    print(f"The integer value is: {number}")
except ValueError:
    # Handle the exception if the input is not a valid integer
    print("Invalid input! Please enter a valid integer.")

# -------------------------------------------------------------------------------------------------

# Exercise 5: (score : 1)
# Write a Python program that prompts the user to input a list of integers and raises
# an exception if any of the integers in the list are negative.
# Prompt the user to input a list of integers
# user_input = input("Please enter a list of integers separated by spaces or commas: ")

#--------------------------------------------------------------------------------------------

# Exercise 6: (score : 2)
# Write a Python program that prompts the user to input a list of integers and
# computes the average of those integers. Use try-except blocks to handle any exceptions that
# might occur.use the finally clause to print a message indicating that the
# program has finished running.
# ----------------------------
#Answer
#------
# try:
#     # Prompt the user to input a list of integers
#     user_input = input("Please enter a list of integers separated by spaces: ")
#
#     # Convert the input string to a list of integers
#     int_list = list(map(int, user_input.split()))
#
#     # Compute the average of the integers
#     average = sum(int_list) / len(int_list)
#
#     print(f"The average of the integers is: {average}")
# except ValueError:
#     print("Invalid input! Please enter a valid list of integers.")
# except ZeroDivisionError:
#     print("Cannot compute the average of an empty list.")
# finally:
#     print("The program has finished running.")

#------------------------------------------------------------------------------------------
#Exercise 7 : (score : 2)
# Write a Python program that prompts the user to input a filename
# and writes a string to that file. Use try-except blocks to handle any exceptions
# that might occur and print a welcome message if there is no exception occurred.
# try:
#     # Prompt the user to input a filename
#     filename = input("Please enter the filename: ")
#
#     # Prompt the user to input the content to write to the file
#     content = input("Please enter the content to write to the file: ")
#
#     # Write the content to the file
#     with open(filename, 'w') as file:
#         file.write(content)
#
#     # Print a welcome message if no exception occurs
#     print("Content written to the file successfully. Welcome!")
# except Exception as e:
#     # Handle any exceptions that might occur
#     print(f"An error occurred: {e}")
#




