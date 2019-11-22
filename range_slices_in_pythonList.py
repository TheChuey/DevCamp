tags = [
    'python',
    'development',
    'tutorials',
    'code',
    'programing',
    'computer science'
]

#tags_range = tags[:-1:2]
tags_range = tags[::-1] # reverses the oder of the list 
# slicing function 
print(tags_range)

"""
# Advanced Techniques for Implementing Ranges and Slices in Python Lists

tag_range = tags[1:-1:2] # we want every other tag here (place in an interval) -inside the bracket you can pass in the third elemnt(interval(every other tag) the 2 takes every other element) 
tag_range = tags[::-1] #slicing -flip the entire order of the list- in bracket-reverse index values-remove second perameter
#above-you would use this 
print(tag_range)
#------------------------------------------------------------------------------
tags.sort(reverse=True) #sorting function looks at the alphabetical value-instead of the above example that pulls the index
print(tags)
////////////////////////////////////////////////////////////

"""