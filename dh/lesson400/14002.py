import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))
dp = [1]*N
result = []

# 1. 최대값 출력
for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

# 2. 리스트 출력
order = max(dp)
lst = []
for i in range(N-1, -1, -1):
    if dp[i] == order:
        lst.append(nums[i])
        order -= 1
lst.reverse()
for i in lst: print(i, end=' ')