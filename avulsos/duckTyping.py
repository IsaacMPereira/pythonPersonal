#Essa é a maior sacanagem dessa linguagem!!

class Animal:
    def speak():
        pass

class Dog(Animal):
    def speak():
        print("Woof!")
    
class Cat(Animal):
    def speak():
        print("Meow!")

class Car:
    def speak():
        print("Vrum!")

animals = [Dog, Cat, Car] 

for animal in animals:
    animal.speak()