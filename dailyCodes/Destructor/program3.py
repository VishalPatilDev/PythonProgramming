class Demo:
    def __init__(self):
        print("In Constructor")
        self.x = 10
        self.y = 20
    def dispData(self):
        print(self.x)
        print(self.y)
    def __del__(self):
        print("In Destructor")
obj = Demo()
obj = Demo()
obj.dispData()
print("End Code")

