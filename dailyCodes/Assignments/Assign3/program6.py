class A:
    def fun(self):
        print("In fun : A")
class B:
    def fun(self):
        print("In fun:B")
class C:
    def fun(self):
        print("In fun:C")
class D(B,C):
    def fun(self):
        print("In fun:D")
        super().fun()


class E(D,A):
    def fun(self):
        print("In fun:E")
        super().fun()

obj = E()
obj.fun()
print(E.mro())



