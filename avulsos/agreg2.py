class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
    
    def addAnimal(self, animal):
        self.animals.append(animal)

    def listAnimals(self):
        return [{f"Name: {animal.name} Race: {animal.race}"} for animal in self.animals]

class Animal:
    def __init__(self, name, race):
        self.name = name
        self.race = race

z1 = Zoo("z1") 

a1 = Animal("name1", "race1")
a2 = Animal("name2", "race2")
a3 = Animal("name3", "race3")

z1.addAnimal(a1)
z1.addAnimal(a2)
z1.addAnimal(a3)

print(z1.listAnimals())
print()

for animal in z1.listAnimals():
    print(animal)