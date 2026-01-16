class Company:
    def __init__(self):
        self.employess = []
    
    def addEmployee(self, employe):
        self.employess.append(employe)
    
    def removeEmployee(self, employe):
        self.employess.remove(employe)

    def listEmployeees(self):
        for employee in self.employess:
            print(employee)