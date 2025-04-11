class Animal:
    def __init__(self, name):
        self.name = name

    __all__ = ['Horse', 'Cat', 'Girafe']

    def eating(self):
        print(f"{self.name} is eating")

    def running(self):
        print(f"{self.name} is running")
    
    def sleeping(self):
        print(f"{self.name} is sleeping")

class Horse(Animal):
    pass

class Cat(Animal):
    pass

class Girafe(Animal):
    pass