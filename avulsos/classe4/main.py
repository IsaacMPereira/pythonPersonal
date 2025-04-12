from vehicle import Vehicle

class car(Vehicle):
    def go(self):
        print("Going with car")

    def stop(self):
        print("Stoping with car")

class moto(Vehicle):
    def go(self):
        print("Going with moto")

    def stop(self):
        print("Stoping with moto")

v1 = car()
v1.go()
v1.stop()

print()
v2 = moto()
v2.go()
v2.stop()
v2.notabs()

if __name__ == "__main__":
    car()
    moto()