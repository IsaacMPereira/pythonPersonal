class Engine:
    def __init__(self, make):
        self.make = make

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, name, engine, wheels):
        self.name = name
        self.engine = Engine(engine)
        self.wheel = [Wheel(wheels) for wheel in range(4)]
    
    def display(self):
        return f"Name: {self.name} Engine: {self.engine.make} Wheels size: {self.wheel[0].size}"

c1 = Car(name="Mustang", engine="Eng1", wheels=18)

print(c1.display())
