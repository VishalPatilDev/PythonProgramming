#private function
class Demo:
    def __init__(self):
        self.x = 10
        self._y = 20
        self.__z = 30
    def __printData(self):
        print(self.x)
        print(self._y)
        print(self.__z)
        print(dir(self.__z))
obj = Demo()
print(dir(Demo))
print(dir(obj))
print(obj.x)
print(obj._y)
print(obj._Demo__z)
obj._Demo__printData()

