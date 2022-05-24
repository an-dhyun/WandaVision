### next permutation 알고리즘

n = int(input())
arr = list(map(int, input().split()))
x = 0

# arr[i-1] < arr[i] 을 만족하는 가장 큰 x = i-1 찾기
for i in range(n-1, 0, -1):
    if arr[i-1] < arr[i]:
        x = i - 1
        break

# i보다 크면서 arr[j] > arr[i-1]을 만족하는 인덱스 번호가 가장 큰 j 찾기
for j in range(n-1, 0, -1):
    if arr[j] > arr[x]:
        arr[j], arr[x] = arr[x], arr[j] # arr[j]와 arr[i-1] swap
        arr = arr[:x+1] + sorted(arr[x+1:]) # arr[i]부터 오름차순으로 정렬
        print(*arr)
        exit()

print(-1)
