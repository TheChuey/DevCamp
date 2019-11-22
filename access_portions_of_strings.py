# The quick brown fox jumped
# T => 0
# h => 1
# e => 2
# ' ' => 3

starter_sentence = 'The quick brown fox jumped'

new_sentence = 'Thy' + starter_sentence[3:]

print(new_sentence)
# accessing a value in a string
# string [index number]
# this statement will return the value
# in the that index in the string
#################################
# you cannot rewrite 
#string [index number] = 'A' // WILL NOT WORK 
# immutability 
##############################
# ranges variable_name[X:X]

"""
first = starter_sentence[0]
second = starter_sentence[1]
third = starter_sentence[2]
new_sentence = first + second + third
print(new_sentence)
"""
first_word = starter_sentence[0:3]
new_sentence = first_word
print(new_sentence)
