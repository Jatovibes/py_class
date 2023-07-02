class School:
    def __init__(self, sname):
        self.school_name = sname

    def display_school_name(self):
        return self.school_name    
    

class MathsClass(School):
    def __init__(self, school):
        super().__init__(school)    

        self.subject = 'Mathematics'

class EngClass(School):
    def __init__(self, school):
        super().__init__(school)

        self.subject = 'English'

class Student(MathsClass, EngClass):
    def __init__(self, name, age, school):
        MathsClass.__init__(self, school=school)
        EngClass.__init__(self, school=school)

        self.student_name = name
        self.student_age = age

john = Student('John', 28 , 'Kings College')    
print(john.display_school_name())    
    