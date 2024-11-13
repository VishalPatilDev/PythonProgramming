class Parent:
    def __del__(self):
        print("In destructor")
obj1 = Parent()
obj2 = Parent()
obj3=obj1
del obj2