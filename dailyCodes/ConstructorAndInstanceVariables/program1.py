class Employee:
    def __init__(self):
        print("In Constructor")
        self.empId = 12
        self.empName = "Kanha"
    def empInfo(self):
        print(self.empId)
        print(self.empName)
emp = Employee()
emp.empInfo()
