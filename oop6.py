class Company:
    def __init__(self, company_name):
          self.company_name = company_name
        
    def company_profile(self):
          print(self.company_name)
          

class Employee(Company):
      def __init__(self, name, company_name):
            super().__init__(company_name)
            self.name = name 
            self.salary = 50000

class Manager(Company):
      def __init__(self, name, company_name):
            super().__init__(company_name)
            self.name = name
            self.salary = 100000

class ChiefExecutive(Company):
      def __init__(self, name, company_name):
            super().__init__(company_name)
            self.name = name
            self.salary = 1000000

john = Employee('John', 'FIRS')    
james = Manager('James', 'FIRS')   
jack= ChiefExecutive('Jack', 'FIRS') 
jack.name='Jack'    


jack.company_profile()
