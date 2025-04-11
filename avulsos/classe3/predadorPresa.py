class Animal:
    def eat(self):
        print("Eating")

    def breath(self):
        print("Breathing")

class Predador(Animal):
    def caca(self):
        print("Esse animal preda")

class Presa(Animal):
    def foge(self):
        print("Esse animal foge")

class Aguia(Predador):
    pass

class Rato(Presa):
    pass

class Peixe(Predador, Presa):
    pass

aguia1 = Aguia()
print("Aguia:")
aguia1.caca()
aguia1.eat()
aguia1.breath()
print()

rato1 = Rato()
print("Rato:")
rato1.foge()
print()

rato1 = Peixe()
print("Peixe:")
rato1.caca()
rato1.foge()
rato1.eat()
rato1.breath()