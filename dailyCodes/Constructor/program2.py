#New constructor is replaced by the old one in the same class(Constructors having the same names)
class Demo:
    def __init__(self):
        print("In Constructor1")
    def __init__(self):
        print("In Constructor2")
obj = Demo()

