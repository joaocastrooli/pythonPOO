class Employee:
    def __init__(self, name, position):
        self.__name = name
        self.__position = position

    def calculatSalary(self, salary):
        self.salary = salary
        print(f"Salario: {self.salary}")

    def __str__(self):
        return f"Funcionario: {self.__name} | Função: {self.__position}"