
n = int(input("Enter your value:"))

for u in range(n):
    c = n-u
    for x in range (1,c+1):
        for y in range (x):
            print("*", end=(""))
        print("")
    for x in range(1,c):
        for y in range(c-x):
            print("*", end=(""))
        print("")
