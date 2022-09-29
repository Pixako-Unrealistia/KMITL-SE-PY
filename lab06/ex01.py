import sys


def remarks():
    inp  = int(sys.stdin.readline())

    if inp not in range (0,101):
        raise ValueError

    inp = inp//10

    match inp:
        case 10:
            return("A")
        case 9:
            return("A")
        case 8:
            return("A")
        case 7:
            return("B")
        case 6:
            return("C")
        case 5:
            return("D")
        case _:
            return("F")

print(remarks())
