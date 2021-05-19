class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student('Ankush', 1)
s2 = Student('John0', 2)

# print(s1.name, s1.rollno)
# s1.show()

# s1.lap.brand
# print(s1.lap.brand, s1.lap.cpu, s1.lap.ram)

# lap1 = s1.lap
# lap2 = s2.lap

lap1 = Student.laptop()
lap2 = Student.laptop()
s1.show()

# Student.lap1.show()
# print(id(lap1), id(lap2))