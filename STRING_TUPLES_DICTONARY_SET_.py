####################### String ############################

string = "jesus"
print(string[0])  
# Read a string

string = "Jesus" + "Rodriguez" # Combine two Strings use + operator
print(string)
#Write into a string
############################  List  ###########################################

list_dataType = ["Jesus","Rodriguez", "Ismael", "Martinez"]
print(list_dataType[:3])
# read a List 

list_dataType.append("Ponce")
print(list_dataType)
# write into a list

list_dataType.insert(2, "De Lion") 
print(list_dataType)
# write into a list
#########################  Tuples  ######################################

Tuples_Types = ("A", "B", "C")
print(Tuples_Types[-1])
# Read a tuple 

Tuples_Types =  Tuples_Types + ("D",) # remember the commma
print(Tuples_Types)
# Write into a Tuple (use the power of reassignment)

######################  Tuples  ##########################################

#Three Ways to Remove Elements from a Python Tuple

Tuples_Types = Tuples_Types[:-1]
#Removing element from end
print(Tuples_Types)


Tuples_Types = Tuples_Types[1:]
print(Tuples_Types)
#Removing element from begginning 

Tuples_Types = list(Tuples_Types)
Tuples_Types.remove("B")
Tuples_Types = tuple(Tuples_Types)
print(Tuples_Types)
# Removing specific element (messy/not recommended)
########################  SET  ############################################

Set_Type = {"one", "two", "three"}
print(Set_Type)
# Read into a Set by using "variable = "read" in Set_Type
read = "one" in Set_Type
print(read)
# Returns True if found False if not 
#requires that all of the elements inside of the set are unique

#########################   Dictonary ##########################

dictonary = {
    "jesus": 42,
    "rodriguez": 0,
    "sex": 1
}

# how to read the value from a key "jesus"
print(dictonary)
value = dictonary["jesus"]
print(value)

# how to write into a key from the value rodriguez
dictonary["rodriguez"] = "Martinez"
print(dictonary)

