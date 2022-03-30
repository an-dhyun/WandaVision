# dp : 이 숫자를 기준으로 한 최대 합 값
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [0]*(n)
dp[0] = nums[0]

for i in range(1, n):
    dp[i] = max(dp[i-1]+nums[i], nums[i])

print(max(dp))