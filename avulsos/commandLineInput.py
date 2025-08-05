import sys

def main():
    z = len(sys.argv)
    if z != 3:
        print("Error")
        exit()

    print(f"Numeber of arguments: {z}")

    for i, arg in enumerate(sys.argv):
        if i > 0:
            print(f"Argument {i}: {arg}")

if __name__ == '__main__':
    main()