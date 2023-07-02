class Company:
    def __init__(self, company_name):
        self.company_name = company_name

    def profile(self):
        print(self.company_name)

class Work(Company):
    def __init__(self, occupation, company):
        super().__init__(company)

        self.occupation = occupation

    def work_profile(self):
        print(f"The company {self.company} has {self.occupation}")   

class Employee(Work):
    def __init__(self, salary, name, company, work):     
        super().__init__(work, company)   

        self.ename = name
        self.salary = salary

    def staff_profile(self):
        print(f"{self.name} works in {self.company} as {self.occupation}")

john = Employee(100000, 'John', 'FIRS', 'Tech Engineer')
print(john.company_name)     