from abc import ABC, abstractclassmethod

class Computer(ABC):
    @abstractclassmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("its running")

# class WhiteBoard(Computer):
#     def write(self):
#         print('its writing')

class Programmer:
    def work(self, com):
        print("Solving bugs")
        com.process()

# com1 = Computer()
# com1.process()

lap1 = Laptop()
# lap1.process()

# whiteB = WhiteBoard()
# whiteB.write()

prog1 = Programmer()
prog1.work(lap1)