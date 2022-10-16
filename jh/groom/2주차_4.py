n, k = map(int, input().split())
arr = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(k):
    a, b = map(int, input().split())
    arr[a][b] += 1
    if a + 1 <= n:
        arr[a + 1][b] += 1
    if a - 1 > 0:
        arr[a - 1][b] += 1
    if b + 1 <= n:
        arr[a][b + 1] += 1
    if b - 1 > 0:
        arr[a][b - 1] += 1

print(sum(sum(arr, [])))