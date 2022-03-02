t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    if n % h == 0:
        y = h
        x = n // h
    else:
        y = n % h
        x = n // h + 1
    print(y*100+x)