def outer():
    def inner1(x,y):
        print("inner1")
        return x+y
    def inner2(x,y):
        print("inner2")
        return x*y
    return inner1,inner2
inn1,inn2 = outer()
ret1 = inn1(10,20)
ret2 = inn2(3,4)
print(ret1+ret2)
print(inn1)
print(inn2)
