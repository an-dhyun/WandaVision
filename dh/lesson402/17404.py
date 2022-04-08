import sys

N = int(sys.stdin.readline())
costs = []
for _ in range(N):
    costs.append(list(map(int, sys.stdin.readline().strip().split())))
INF = 2147000000
ans = INF

for i in range(3):
    dp = [[INF, INF, INF] for _ in range(N)]
    # dp : 각각 시작이 R, G, B일 때 n번째 집까지 칠하는 비용의 최소값
    dp[0][i] = costs[0][i]

    for j in range(1, N):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + costs[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + costs[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + costs[j][2]
    
    for j in range(3):
        if i!=j: 
            ans = min(ans, dp[-1][j])
print(ans)
