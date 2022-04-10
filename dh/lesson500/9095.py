import sys

dp = [0]*12
dp[0] = dp[1] = 1
dp[2] = 2
for i in range(3, 12):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    print(dp[n])
