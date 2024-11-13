class Demo:
    z = 30
    def __init__(self):
        self._x = 10
        self.__y = 20   #_Demo__y
print(dir(Demo))
obj = Demo()
print(dir(obj))
