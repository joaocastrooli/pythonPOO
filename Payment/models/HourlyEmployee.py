from models.Employee import Employee

class HourlyEmployee(Employee):
    def __init__(self, name, position, hoursWorked, hourlyRate):
        super().__init__(name, position)
        self.__hoursWorked = hoursWorked
        self.__hourlyRate = hourlyRate

    def calculatSalary(self, hourlyRate, hoursWorked):
        return (hourlyRate * hoursWorked)