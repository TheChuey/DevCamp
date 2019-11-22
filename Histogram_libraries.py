value = {
    "g": 10,
    "f": 20,
    "t": 30,
    "o": 40,
}
#for key, value in value.items():
#   print(key, (value * "$"))

#name = value.get(letter)
#second = name * 'g'

print('g ' + sales['google'] * '$')
print('f ' + sales['facebook'] * '$')
print('t ' + sales['twitter'] * '$')
print('o ' + sales['offline'] * '$')

#Iterating Through .values()
#It’s also common to only use the values to iterate through a dictionary in Python.
# One way to do that is to use .values(), which returns a view with the values 
# of the dictionary:

#Iterating Through .keys()
#If you just need to work with the keys of a dictionary, then you can use .keys(),
#which is a method that returns a new view object containing the dictionary’s keys:

