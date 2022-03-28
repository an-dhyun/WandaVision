import sys
input = sys.stdin.readline

n = int(input())
p = [0] + list(map(int, input().split()))
dp = [x*n for x in p]

for i in range(1, n+1):
    for k in range(1, i+1):
        dp[i] = min(dp[i], dp[i-k] + p[k])

print(dp[i])