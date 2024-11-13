class Employee:
    def __init__(self,empId,empName):
        print("In Constructor")
        self.empId = empId
        self.empName = empName
    def empInfo(self):
        print(self.empId)
        print(self.empName)
emp = Employee(100,"Rahul")
emp.empInfo()
