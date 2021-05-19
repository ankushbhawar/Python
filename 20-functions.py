def hey():
    print("hello")
hey()

def f1(marks):
    return (sum(marks)/400)*100

marks1 = [1,2,3,4]
marks2 = [92,91,94,93]
percent = f1(marks1)
percent2 = f1(marks2)
print(percent)
print(percent2)

def greeting(name = "User"):
    print("Hello " + name)

name = input("Enter your name ")
greeting(name)

def sum(num1, num2):
    return num1 + num2

print(sum(5,5))