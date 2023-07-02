class Animal:
    def __init__(self, name, age, sex, breed):
        self.name = name
        self.age = age
        self.sex = sex
        self.breed = breed

    def sound(self):
        if self.name =='cat':
            print('Meow')
        elif self.name == 'dog':
            print('bark')    
        else:    
            print("Don't know sound")

    def get_profile(self):
        print(f"The {self.name} is a {self.sex} and its {self.age} years old which is of a {self.breed} breed")

    def profile(self):
        self.get_profile()    



dog = Animal('dog', 4, 'Male', 'Samoyed') 
dog.age = 15 
print(dog.age)
dog.sound()  
dog.profile()

