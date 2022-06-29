import sys
input = sys.stdin.readline

s = set()
m = int(input())

for _ in range(m):
    temp = input().split()

    if len(temp) == 1:
        if temp[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
        continue
    
    op, x = temp[0], temp[1]
    x = int(x)

    if op == 'add':
        s.add(x)
    elif op == 'remove':
        s.discard(x)
    elif op == 'check':
        print(1 if x in s else 0)
    elif op == 'toggle':
        if x in s:
            s.discard(x)
        else:
            s.add(x)