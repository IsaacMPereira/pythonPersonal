__all__ = ['Horse', 'Cat', 'Girafe']

class Animal:
    def __init__(self, name):
        self.name = name

    def eating(self):
        print(f"{self.name} is eating")

    def running(self):
        print(f"{self.name} is running")
    
    def sleeping(self):
        print(f"{self.name} is sleeping")

class Horse(Animal):
    def __init__(self, name):
        super().__init__(name)

    def trotting(self, times):
        print(f"The horse is trotting {times} times")

class Cat(Animal):
    pass

class Girafe(Animal):
    pass