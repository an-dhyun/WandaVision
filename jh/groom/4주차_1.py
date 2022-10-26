n, m = map(int, input().split())
wait = list()
for i in range(m):
    a, b = input().split()
    b = int(b)
    if a == 'deposit':
        n += b
        while wait and n >= wait[0]:
            n -= wait.pop(0)

    if a == 'pay':
        if n >= b:
            n -= b

    if a == 'reservation':
        if wait:
            wait.append(b)
        else:
            if n >= b:
                n -= b
            else:
                wait.append(b)
print(n)
