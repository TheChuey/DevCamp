name = "kristine"
age = "12"
product = "Python elearning course"

#greeting = "Hi {0}, you are listed as {1} years {3} old and you have purchased: {2}...".format(name, age, product, "jesus")
greeting = f"Hi {name}, you are listed as {age} years old and you have purchased: {product}..."
print (greeting)

# started off with a few variables line 1 - 3 
# then created a greeting then said we want the product purchased with 2 because it's the product number 3 in the list after the .format
# format takes in any amount of arguments to pass in and then maps to the values
# name is the zero index, age is the 1st index, product is the 2nd index, and Jordan is the 3rd index here
# the second greeting references to the variables directly
# easier way to use string interpolation

"""
str.format(*args, **kwargs)
Perform a string formatting operation. The string on which this method is called can contain literal text or 
>replacement fields delimited by braces {}. Each replacement field contains either the numeric index of a positional
>argument, or the name of a keyword argument. Returns a copy of the string where each replacement field is 
>replaced with the string value of the corresponding argument.
"""
