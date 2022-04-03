import sys

input = sys.stdin.readline

n = int(input())
dp = [[0] * 3 for _ in range(n)]
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))
print(dp)
print(cost)

m = float('inf')
for j in range(3):
    for i in range(3):
        if j == i:
            dp[0][i] = cost[0][i]
        else:
            dp[0][i] = float('inf')

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

    for i in range(3):
        if i == j:
            continue
        m = min(m, dp[n-1][i])

print(m)