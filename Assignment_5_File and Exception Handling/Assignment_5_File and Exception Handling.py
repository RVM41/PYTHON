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
file_path = "C:\\Users\\pc\\OneDrive\\Desktop\\New folder\\python.txt"

# Initialize a variable to count the words
word_count = 0

# Open the file in read mode
file = open(file_path, 'r')

# Read the contents of the file
contents = file.read()

# Split the contents into words
words = contents.split()

# Count the number of words
word_count = len(words)

# Close the file
file.close()

# Display the total number of words
print(f"Total number of words: {word_count}")

