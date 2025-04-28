z = int(input())

while z != 1:
    if(z % 2 == 0): 
        z /= 2
        print(z)
    elif(z % 2 != 0): 
        z = (3 * z) + 1
        print(z)