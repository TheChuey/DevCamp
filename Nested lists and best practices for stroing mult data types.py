users = ['kristine', 'Tiffany', 'Jordan', 'lean']
ids = [1,2,3,4]
mixed_list = [42, 10.3, 'Altuve']
print(mixed_list)

user_list = mixed_list.pop()

print(user_list)
print(mixed_list)

# nested collections of list 
# best practices line 3 its dangerous mixed data types
# The program will breack so be careful when using mix data types list

nested_list = [ [123], [456], [789]]

print (nested_list)

"""
users = ['Kristine', 'Tiffany', 'Jordan', 'Leann'] # list of strings
ids = [1,2,3,4] # list of integers 

mixed_list = [42, 10.3, 'Altuve', users] # first element is an integer, then a float, then a string, then call users to slide the list of users

print(mixed_list)

user_list = mixed_list.pop() # will pop off the list users and print all the list names

print(user_list)
print(mixed_list)

nested_list = [[123], [234], [345]] 
"""