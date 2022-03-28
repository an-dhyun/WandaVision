n = int(input())
a = list(map(int, input().split()))
arr = [a[0]]
for i in range(len(a)-1):
    arr.append(max(arr[i] + a[i+1], a[i+1]))
print(max(arr))