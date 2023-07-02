class Scores:
    def __init__(self, numbers):
        self.numbers = numbers

    def score(self):
        new_dict = {}
        for name in self.numbers:
            if self.numbers[name] >= 70:
                new_dict[name] = 'A'
            elif self.numbers[name] >= 60:
                new_dict[name] = 'B'
            elif self.numbers[name] >= 50:
                new_dict[name] ='C'
            else:
                new_dict[name] = 'D'   

        return new_dict


student_grades = Scores({'John' : 87, 'James' : 54, 'Josh' : 75, 'Mary' : 39})
print(student_grades.score())

