import sys
tempo = []
tempo.extend(reversed(list(sys.stdin.readline().strip())))
if len(tempo) != 4:
    raise ValueError
for x in tempo:
    sys.stdout.write(x)
