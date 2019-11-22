#How to Use a Tuple as a Dictionary Key in Python
# combine all three of the data structures
# usualy keys are strings but they can be multiple items

priority_index = {
  (1, 'premier'): [1, 34, 12],
  (1, 'mvp'): [84, 22, 24],
  (2, 'standard'): [93, 81, 3],
}

print(list(priority_index.keys()))

#keys() method in a Python Dictionary, 
#returns a view object that displays a list of all the keys in the dictionary.
#The list() constructor returns a mutable sequence list of elements. The iterable argument is optional. 
