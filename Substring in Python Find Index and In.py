sentence = "The quick brown fox jumpes over the lazy dog."

query = sentence.find("quick")
print(query)
"""
EXTRA NOTES TO HOLD ON TO

str.find(sub[, start[, end]])
Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments >start and end are interpreted as in slice notation. Return -1 if sub is not found

Note
The find() method should be used only if you need to know the position of sub. To check if sub is a substring or >not, use the in operator

str.index(sub[, start[, end]])
Like find(), but raise ValueError when the substring is not found.
"""

