# Uniqueness
tags = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

print(tags)

# Nope
#print(tags[0]) does not work like a dictornary 

query_one = 'python' in tags  # looks up an item on a set 
query_two = 'ruby' in tags # looks up and find nothing 

# Returns a True or False if in finds what its looking for

print(query_one)
print(query_two)