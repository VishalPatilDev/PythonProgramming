class Boss:
    def report(self):
        print("Boss : Report")
class Manager1(Boss):
    def report(self):
        print("Manager1 : Report")
class Manager2(Boss):
    def report(self):
        print("Manager2 : Report")
class Manager3(Boss):
    def report(self):
        print("Manager3 : Report")
class TeamLead1(Manager1,Manager2):
    def report(self):
        print("TeamLead1 : Report")
class TeamLead2(Manager2,Manager3):
    def report(self):
        print("TeamLead2 : Report")
class Developer(TeamLead1,TeamLead2):
    def report(self):
        print("Developer : Report")
obj = Developer()
obj.report()
#print(Developer.__mro__)
print(Developer.mro())
