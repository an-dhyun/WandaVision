import sys
N = int(sys.stdin.readline())
costs = []
for _ in range(N):
    costs.append(list(map(int, sys.stdin.readline().strip().split())))

dp = [[0 for _ in range(3)] for _ in range(N)]
dp[0] = costs[0] # 하나만 칠할땐 그냥 넣음

for i in range(N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

print(min(dp[N-1]))