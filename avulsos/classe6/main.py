from shapePoly import *

def main():
    shapes = [Circle(6), Square(9), Triangle(14, 4)]    

    for shape in shapes:
        print(f"{shape.area()} cm")

if __name__ == "__main__":
    main()