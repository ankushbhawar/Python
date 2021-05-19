# f = open("sample.txt", "r")
# data = f.read() # read(5), readline()
# print(data )
# f.close()

# f2 = open("sample2.txt", "a")
# newData = f2.write(" Please write this to the file")
# f2.close()

with open("sample.txt", "r") as f3:
    a = f3.read()
    print(a)

with open("sample.txt", "w") as f4:
    b = f4.write("hello world")
    print(b)