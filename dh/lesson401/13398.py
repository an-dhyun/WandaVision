import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

dp = [[0 for _ in range(N)] for _ in range(2)]
dp[0][0], dp[1][0] = nums[0], nums[0]
# 0 : 아무 원소도 제거하지 않음
# 1 : 특정 원소를 제거한 시점

for i in range(1, N):
    dp[0][i] = max(dp[0][i-1] + nums[i], nums[i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + nums[i])

print(max(max(dp[0]), max(dp[1])))