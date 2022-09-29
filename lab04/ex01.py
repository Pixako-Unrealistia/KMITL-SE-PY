import sys

inp  = int(sys.stdin.readline())

if inp not in range (0,101):
    raise ValueError

inp = inp//10

match inp:
    case 10:
        sys.stdout.write("A")
    case 9:
        sys.stdout.write("A")
    case 8:
        sys.stdout.write("A")
    case 7:
        sys.stdout.write("B")
    case 6:
        sys.stdout.write("C")
    case 5:
        sys.stdout.write("D")
    case _:
        sys.stdout.write("F")
