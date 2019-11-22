import operator 
import functools
from functools import reduce

"""
dynamic_reudcer([1,2,3], '+') # sum 6
dynamic_reudcer([1,2,3], '-') # sum -
dynamic_reudcer([1,2,3], '*') # sum -
dynamic_reudcer([1,2,3], '/') # sum -

"""
number = [1,2,3]

print ("# sum",  functools.reduce(operator.add, number))
print ("# sum", functools.reduce(operator.sub, number))
print ("# sum", functools.reduce(operator.mul, number))
print ("# sum", functools.reduce(operator.truediv, number))


"""
import operator
from functools import reduce

def dynamic_reducer(collection, op):   #<---function called dymanic reducer and takes in a collection and op 
    operators = {                # create the dictionary called operators with CURLY BRACES (look up table) set of key value pairs
        "+": operator.add,       # value is calling the operator library and calling add in it
        "-": operator.sub,       # same thing just calling subtract
        "*": operator.mul,       # then multiply 
        "/": operator.truediv,   # then divide
    }
    #below-now to use the reduce library say return and call the reduce function-it takes in 2 functions(fist is lambda it has a total and an element)
    #then say operators use look up syntax and call op(second argument), now expects the second argument collection
    return reduce((lambda total, element: operators[op](total, element)), collection)

print(dynamic_reducer([1, 2, 250], '+'))
print(dynamic_reducer([1, 2, 3], '-'))
print(dynamic_reducer([1, 2, 55], '*'
From Benjamin Nicklaus to Everyone:  03:27 PM
print(dynamic_reducer([100, 2, 3], '/'))
////////////////////////////////////////////////////////////////////
"""
