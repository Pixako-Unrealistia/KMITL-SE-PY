import sys

sys.stdout.write("""Please input in the following format: (x,y)\nFirst tuple shall be the first point,
second being the second point and third being desired point""")
#example of valid inputs
#(100,200)
#(-100,200)
#(-140,100)

for x in range(3):
    sys.stdout.write(f"\n")
    exec(f"{chr(65 + x)} = eval(sys.stdin.readline())")

x = (A[0] + B[0]) / 2
y = (A[1] + B[1]) / 2

if C[0] > x:
    sys.stdout.write("Right\n")
elif C[0] < x:
    sys.stdout.write("Left\n")
elif (C[0] == x) and (C[1] == y):
    sys.stdout.write("Your point is on the line between the two points\n")
else:
    sys.stdout.wrote("Your point is neither at left nor right side, nor is it on the line.")
#print("Debug info\n",x,y)