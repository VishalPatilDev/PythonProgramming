class Demo:
    def __init__(self):
        self.x = 10
class DemoChild(Demo):
    def __init__(self):
        self.y = 20
        super().__init__()
    def dispData(self):
        print(self.x)
        print(self.y)
obj = DemoChild()
obj.dispData()
