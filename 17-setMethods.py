a = set()
print(type(a))

a.add(27)
print(a)

print(type(a))
a.add((1,2,3,4))
a.add((1,2,3,5))
a.add((1,2,3,4))

a.add(4)
print(a)

print(len(a))
a.add(2)
print(a)

a.remove(4)
print(a)

print(a.pop())
print(a)

s = {18, "18"}
print(s)
print(type(s))

s2 = set()
s2.add(20)
s2.add(20.1)
s2.add("20")

print(s2)
print(len(s2))