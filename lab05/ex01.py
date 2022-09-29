import sys

if (sys.stdin.readline().strip() == "A"):
    for k in range(1,6):
        for x in range(1,k+1):
            sys.stdout.write(str(x))
        sys.stdout.write("\n")
else:
    for k in range(1,6):
        for x in range(1, 7-k):
            sys.stdout.write(str(x))
        sys.stdout.write("\n")
