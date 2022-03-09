import sys
for _ in range(100):
    sent = list(sys.stdin.readline().rstrip('\n'))
    higher, lower, num, space = 0, 0, 0, 0
    for i in sent:
        if i.islower(): lower += 1
        elif i.isupper(): higher += 1
        elif i.isdigit(): num += 1
        elif i.isspace(): space += 1
    print(lower, higher, num, space)