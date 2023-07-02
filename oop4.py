class Father:
    def __init__(self,fname):
        self.father_name = fname

    def fathers_occupation(self):
        print("Engineering")     

class Mother:
    def __init__(self, mname):
        self.mother_name = mname

    def mothers_occupation(self):
        print('Nursing')

class Child(Father, Mother):
    def __init__(self, cname, fname, mname):
        Father.__init__(self, fname)  
        Mother.__init__(self, mname)
                           

        self.child_name= cname

john = Child("John","James", "Jane")
john.fathers_occupation()
john.mothers_occupation()
print(john.mother_name)