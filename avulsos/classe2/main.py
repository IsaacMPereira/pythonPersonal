from animal import Horse
from animal import Cat
from animal import Girafe
#from animal import Horse, Cat, Girafe
#from animal import * #Restricted by __all__ method in animal.py

def main():
    h1 = Horse("h1")
    c1 = Cat("c1")
    g1 = Girafe("g1")

    h1.eating()
    h1.running()
    h1.sleeping()
    h1.trotting(500)
    print()

    c1.eating()
    c1.running()
    c1.sleeping()
    print()

    g1.eating()
    g1.running()
    g1.sleeping()
    print()

if __name__ == "__main__":
    main()