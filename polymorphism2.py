class Manager:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def profile(self):
        return f"{self.name} get paid ${self.salary}"

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary   

    def profile(self):
        return f"{self.name} get paid ${self.salary}"
    
john = Manager('John', 20000)
james = Employee('James',150000)    

management = [john, james]

for member in management:
    print(member.profile())
 