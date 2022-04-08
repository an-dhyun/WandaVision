for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    cnt = 1

    while (x <= m*n):
        if (x-y)%n == 0:
            print(x)
            cnt = 0
            break
        x += m
    if cnt:
        print(-1)