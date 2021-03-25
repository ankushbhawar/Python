# display a user entered name followed by good afternoon unsing input function
print("program 1")
name = input("Enter your name : ")
print("Good Afternoon, ", name)

# fill in a letter template given below with name and date
print("Program 2")
letter = '''Dear <|NAME|>,
You are selected!
Date: <|DATE|>
'''
name_2 = input("Please enter your name : ")
date = input("Enter date : ")
letter = letter.replace("<|NAME|>", name_2)
letter = letter.replace("<|DATE|>", date)
print(letter)

# detect double space in a string 
print("Program 3")
string_1 = "Hey, This is  Ankush"
print(string_1.find("  "))

# detect double space in a string and replace it with single spaces 
print("Program 4")
string_2 = "Hey, This is  Ankush"
print(string_2)
print(string_1.replace("  ", " "))

''' formate the following letter using escape sequence chacters,
letter = "Dear John, This Python Course is nice! Thanks! '''
print("Program 5")

letter_2 = "Dear John,\n\t This Python Course is nice!\nThanks!"
print(letter_2)