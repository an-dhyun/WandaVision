a, b, c = map(int, input().split())
i = 1
if b >= c:
    print(-1)
else:
    print(int(a/(c-b)+1))