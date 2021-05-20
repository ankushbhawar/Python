class A:

    def __init__(Self):
        print('In A init')

    def feature1(self):
        print('feature 1-A workng')

    def feature2(self):
        print('feature 2-A workng')

class B():

    def __init__(Self):
        # super().__init__()
        print('In B init')

    def feature1(self):
        print('feature 1-B workng')

    def feature2(self):
        print('feature 2-B workng')

class C(A,B):
    def __init__(self):
        super().__init__()
        print("In C init")

    def feat(self):
        super().feature2()

a1 = C()
a1.feat()