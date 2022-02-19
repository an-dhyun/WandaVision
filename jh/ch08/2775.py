t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    floor_0 = [x for x in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            floor_0[j] += floor_0[j-1]
    print(floor_0[-1])