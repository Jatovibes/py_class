class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):    
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.bonus = 10/100

    def get_salary(self):
        return self.salary*self.bonus

class Engineer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.bonus = 5/100

    def get_salary(self):
        return self.salary*self.bonus  


def payroll(employees):
    for i in employees:
        print(f"Name: {i.name} Salary: {i.get_salary()}")
        


employees = [Manager('John', 50000), Engineer('Scott', 70000),]

payroll(employees)