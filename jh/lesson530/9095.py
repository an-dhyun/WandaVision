t = int(input())

def sum123(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sum123(n-3) + sum123(n-2) + sum123(n-1)

for _ in range(t):
    n = int(input())
    print(sum123(n))
