import sys
n = int(sys.stdin.readline()) 
cost = [0] + [int(sys.stdin.readline()) for _ in range(n)]
dp = [0]*(n+1) # 각 자리별 최대값

dp[1] = cost[1]
if n>1: # n=1이면 오류발생
    dp[2] = cost[1] + cost[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-3]+cost[i-1]+cost[i], dp[i-2]+cost[i])

print(dp[n])