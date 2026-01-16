from models.Employee import Employee
from models.HourlyEmployee import HourlyEmployee
from models.SalariedEmployee import SalariedEmployee
from models.Company import Company

castro = Company()
funcionario1 = Employee("João", "Estagiario")
castro.addEmployee(funcionario1)
castro.listEmployeees()
