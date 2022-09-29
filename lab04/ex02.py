import sys

k = sys.stdin.readline()

if "." in k:
    k = float(k)
    sys.stdout.write("Type A if you want to display in floating, B for scientific notation\n")

    if sys.stdin.readline().strip() == "A":
        sys.stdout.write(f"{k}") #stdout can't write non-string :/
    else:
        sys.stdout.write(f"{k:.2E}")
else:
    k = int(k)
    sys.stdout.write("A for binary, B for octal, C for hexadecimal, D for decimal\n")
    
    match sys.stdin.readline().strip():
        case "A":
            sys.stdout.write(f"{bin(k)[2:]}") #nozfill?
        case "B":
            sys.stdout.write(f"{oct(k)[2:]}")
        case "C":
            sys.stdout.write(f"{hex(k)[2:]}")
        case "D":
            sys.stdout.write(f"{k}")           
        case _:
            raise ValueError
