import sys
n = int(sys.stdin.readline())
dp = [0]*(n+1)
dp[0] = dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%10007)

# 개수 잘못 세서 삽질했다 ..