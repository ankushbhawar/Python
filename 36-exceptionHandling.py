a = 5
b = 2

try:
    print("resource open")
    print(a/b)

    k = int(input("Enter a number"))
    print(k)

except ZeroDivisionError as e:
    print("Hey you cannot devide a number by zero,", e)

except ValueError as e:
    print("Invalid input")

except Exception as e:
    print("Something went wrong,", e)

finally:
    print("resource closed")

print("Bye")