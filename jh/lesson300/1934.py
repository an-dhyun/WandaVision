t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    c = a * b
    while b > 0:
        r = a % b
        a = b
        b = r
    print(int(c/a))