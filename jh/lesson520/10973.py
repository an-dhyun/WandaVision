n = int(input())
arr = list(map(int, input().split()))
x = 0

for i in range(n-1, 0, -1):
    if arr[i-1] > arr[i]:
        x = i-1
        break

for j in range(n-1, 0, -1):
    if arr[j] < arr[x]:
        arr[j], arr[x] = arr[x], arr[j]
        arr = arr[:x+1] + sorted(arr[x+1:], reverse=True)
        print(*arr)
        exit()

print(-1)