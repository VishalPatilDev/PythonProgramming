class BCCI:
    def ballsInOver(self):
        print("6 balls in a over")
    def rules(self):
        print("BCCI rules")
    
class IPL(BCCI):
   pass
obj = IPL()
obj.ballsInOver()
obj.rules()
