c = 0
k = 0
for x in range(0,5):
    k = int(input("Please enter an integer: "))
    if (k > 0 and c < 0) or (k < 0 and c > 0):
        c = 0
    c += k
    print(f"current sum = {c}")
