
k = int(input("Enter number of lines: "))

topple = round(k/2) 

for x in range(0,topple):
    print(" ".join(reversed([str(2**z) for z in range(0,x+1)])))
    #technically nested for loop right?
for y in range(topple, k+1):
    print(" ".join(reversed([str(2**z) for z in range(0,k-y)])))
