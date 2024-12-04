'''
Data structures in python

Topic :List
Exercise
Q1. Create a list of 5 random numbers and print the list.
Q2. Insert 3 new values to the list and print the updated list.
Q3. Try to use a for loop to print each element in the list.

Topic: Dictionary
Exercise
Q1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively.
Q2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'.

Topic: Set
Exercise
Q1.Create a set with values 1, 2, 3, 4, and 5.
Q2. Add the value 6 to the set created in Q1.
Q3. Remove the value 3 from the set created in Q1.

Topic:Tuple
Exercise
Q1. Create a tuple with values 1, 2, 3, and 4
Q2. Print the length of the tuple created in Q1.
'''
#
# # Topic :List
# # Exercise
# # Q1. Create a list of 5 random numbers and print the list
# import random
# random_list = [random.randint(1, 100) for _ in range(5)]
# print("Original list:", random_list)
# print (type (random_list))
#
# # Q2: Insert 3 new values to the list and print the updated list
# new_values = [random.randint(1, 100) for _ in range(3)]
# random_list.extend(new_values)
# print("Updated list:", random_list)
#
# #Q3: Use a for loop to print each element in the list
# for number in random_list: print(number)

# Topic: Dictionary
# Q1: Create a dictionary
# person = { 'name': 'John', 'age': 25, 'address': 'New York' }
# print("Original dictionary:", person)
#
# # Q2: Add a new key-value pair to the dictionary
# person['phone'] = '9847869565'
# print("Updated dictionary:", person)

# Topic: Set
# # Q1: Create a set
# my_set = {1, 2, 3, 4, 5}
# print("Original set:", my_set)
#
# # Q2: Add the value 6 to the set
# my_set.add(6)
# print("Set after adding 6:", my_set)
#
# # Q3: Remove the value 3 from the set
# my_set.remove(3)
# print("Set after removing 3:", my_set)

# Topic:Tuple

# Q1: Create a tuple
my_tuple = (1, 2, 3, 4)
print("Tuple:", my_tuple)

# Q2: Print the length of the tuple
print("Length of the tuple:", len(my_tuple))


