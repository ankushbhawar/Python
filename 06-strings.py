''' string : string is a data type in python and string is a sequence of characters enclosed in quotes.
we can primarily write a string in these three ways : single quoted strings, double quoted strings and triple quoted strings
'''

# concatination
print("String concatination")
greeting = "Good Morning, "
name = "Ankush"
print(greeting + name)

# string slicing
print("String slicing")
string_1 = "Hello"
print(string_1[1])
print(string_1[0:3])
print(string_1[:2])
print(string_1[0:])

# negative indexes
print("Negative indexes")
print(string_1[-5: -3])

# slicing with skip value
print("Slicing with negative values")
print(string_1[0::2])