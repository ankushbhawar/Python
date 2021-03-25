# string functions
print("String functions")
story = "what is up everybody, This is Ankush.."

# string length
print("String length")
print(len(story))

# is string ends with
print("Is string ends with")
print(story.endswith("Ankush.."))

# string count
print("String counts")
print(story.count("A"))
print(story.count("is"))

# string capitalize
print("String capitalize")
print(story.capitalize())

# find
print("Find")
print(story.find("Ankush"))

# replace
print("Replace")
print(story.replace("Ankush", "Anku"))

# escape sequence
print("Escape sequence")
story_2 = "Hello, \nThis is \tAnkush \nWhat\'s \\ what is going on."
print(story_2)