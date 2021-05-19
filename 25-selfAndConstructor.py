class Computer:
    def __init__(self):
        self.name = "Ankush"
        self.age = 23

    def update(self):
        self.age = 24
    
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c2 = Computer()

# print(id(c1))
# print(id(c2))

# print(c1.name)
# print(c1.age)
# print(c2.name)
# print(c2.age)

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

c1.name = "John"
c1.update()

# print(c1.name)
# print(c1.age)

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")