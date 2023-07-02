class Animal:
    def __init__(self, name):
        self.name = name


    def sound(self):
        print('animal.sound')



class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self, name)


    def eat(self):
        print('eating')   



bull_dog = Dog('Bull Dog')
bull_dog.eat()
bull_dog.sound()
print(bull_dog.name)