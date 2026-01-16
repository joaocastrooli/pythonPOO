from models.Employee import Employee

class SalariedEmployee(Employee):
    def __init__(self, name, position, salary):
        super().__init__(name, position)
        self.__salary = salary