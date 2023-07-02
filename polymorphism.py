class Organization:
    def __init__(self, org_name):
        self.org_name = org_name

class Employee1(Organization):
    def __init__(self, ename, org_name):
        Organization.__init__(self, org_name)
        self.employee = ename

class Employee2(Organization):
    def __init__(self, ename, org_name):
        Organization.__init__(self, org_name)
        self.employee = ename

class Manager(Employee1, Employee2):
    def __init__(self, ename1, ename2, org_name):
        Employee1.__init__(self, ename1, org_name)
        Employee2.__init__(self, ename2, 'FIRS')
        

james = Manager('John', 'Alex', 'NNPC')  
print(james.employee)      
print(james.org_name)      

    