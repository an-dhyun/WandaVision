import sys
input = sys.stdin.readline

dp = [1] * 10
n = int(input())
for i in range(n-1):
    for j in range(1, 10):
        dp[j] += dp[j-1]

print(sum(dp) % 10007)