import sys
sys.stdout.write("""
First prompt: Input in (x,y) format
Second prompt: Input for width
Third prompt" Input for height\n
First rectangle:\n""")

for x in range(3):
    sys.stdout.write(f"\n")
    exec(f"{chr(65 + x)} = eval(sys.stdin.readline())")

sys.stdout.write("Second rectangle")

for x in range(3,6):
    sys.stdout.write(f"\n")
    exec(f"{chr(65 + x)} = eval(sys.stdin.readline())")

first = []
second = []
first.append([A[0] + (B/2), A[1] + (C/2)])
first.append([A[0] - (B/2), A[1] - (C/2)])
first.append([A[0] + (B/2), A[1] - (C/2)])
first.append([A[0] - (B/2), A[1] + (C/2)])

second.append([D[0] + (E/2), D[1] + (F/2)])
second.append([D[0] - (E/2), D[1] - (F/2)])
second.append([D[0] + (E/2), D[1] - (F/2)])
second.append([D[0] - (E/2), D[1] + (F/2)])

#print(first,"\n",second)

checker = 0

if first[0][1] <= second[0][1] and first[0][1] >= second[1][1]:
    if first[0][0] <= second[0][0] and first[0][0] >= second[1][0]:
        if first[1][1] <= second[0][1] and first[1][1] >= second[1][1]:
            if first[1][0] <= second[0][0] and first[1][0] >= second[1][0]:
                print("First rectangle is in the second.")
                checker = 1

if second[0][1] <= first[0][1] and second[0][1] >= first[1][1] and checker == 0:
    if second[0][0] <= first[0][0] and second[0][0] >= first[1][0]:
        if second[1][1] <= first[0][1] and second[1][1] >= first[1][1]:
            if second[1][0] <= first[0][0] and second[1][0] >= first[1][0]:
                print("Second rectangle is in the first.")
                checker = 1

if second[0][1] <= first[0][1] and second[0][1] >= first[1][1] and checker == 0:
    print("The rectangles overlapped.")
    checker = 1
elif second[0][0] <= first[0][0] and second[0][0] >= first[1][0] and checker == 0:
    print("The rectangles overlapped.")
    checker = 1

#has to do this otherwise the line would be too long :/

if first[0][1] <= second[0][1] and first[0][1] >= second[1][1] and checker == 0:
    print("The rectangles overlapped.")
    checker = 1
elif first[0][0] <= second[0][0] and first[0][0] >= second[1][0] and checker == 0:
        print("The rectangles overlapped.")
        checker = 1
