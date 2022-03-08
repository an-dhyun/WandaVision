import sys
input = sys.stdin.readline

while True:
    line = input().rstrip('\n') # only enter remove

    if not line:
        break

    # small letter, captial letter, number, space
    a, b, c, d = 0, 0, 0, 0
    for i in line:
        if i.islower():
            a += 1
        elif i.isupper():
            b += 1
        elif i.isnumeric():
            c += 1
        elif i.isspace():
            d += 1
    print(a,b,c,d)
