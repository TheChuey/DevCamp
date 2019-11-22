 [num for num in num_list if num % 2 == 0]  
# first item passed is the action we want to take
# Second the for in Irratator 
# dynamically generate a lis, by using [condition, for accumlator in counter]


"""
we can set a number for in loops to function on a single line 
and generate list from those lines of code
set of 'for in loops' and conditionals 
"""

num_list = range(1, 11)  # create the num list and say range and you want numbers 1-10
cubed_nums = []          # get the cubed numbers(take all nmbers and cube them)

for num in num_list:          # for num in the the num list
  cubed_nums.append(num ** 3) # cubed nums and append and say num ** 3 which cubes the values

print(list(num_list))

#capture even numbers
num_list = range(1, 11)

even_numbers = []                     # say even numbers ais eqqual to empty list

for num in num_list:                  # condition below
  if num % 2 == 0:                    # if the num is %(tells us if remainder) 2 is equal to zero (is it even)
    even_numbers.append(num)          # take the even numbers and append the numbers
#list comperhension
even_numbers = [num for num in num_list if num % 2 == 0]  # start with square brackets then num for num in the list, then add the condition on the same line

print(even_numbers)

# num is the first element-python says what ever element we are returning is the one we want to add(only if it is even)
"""
start with square brackets to geneertae the list
just combine the condition on the same line
when you use a conditional ( 3 elements before now 4)
if num % 2 == 0 is the condition
"""
#https://bottega.devcamp.com/12/guide/1479

