class A:
    def feature1(self):
        print('feature 1 workng')

    def feature2(self):
        print('feature 2 workng')

class B(A):
    def feature3(self):
        print('feature 3 workng')

    def feature4(self):
        print('feature 4 workng')

class C(B):
    def feature5(self):
        print('feature 5 workng')


class A2:
    def feature7(self):
        print('feature 7 workng')

class D(A, A2):
    def feature6(self):
        print('feature 6 workng')   

a1 = A()
# a1.feature1()
# a1.feature2()

b1 = B()
# b1.feature1()
# b1.feature2()
# b1.feature3()
# b1.feature4()

c1 = C()
# c1.feature1()
# c1.feature2()
# c1.feature3()
# c1.feature4()
# c1.feature5()

a2 = A2()
# a2.feature7()

d1 = D()
d1.feature1()
d1.feature2()
d1.feature7()
d1.feature6()