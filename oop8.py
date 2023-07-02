class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary


    def show_salary(self):
        return self.__salary   

class Work(Employee):
    def __init__(self, ename, esalary, work):
        super().__init__(ename, esalary)

        self.work = work


john = Employee('John', 100000)
print(john._Employee__salary)