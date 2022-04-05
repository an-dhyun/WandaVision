import sys
N, K = map(int, sys.stdin.readline().split())
dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

dp[1] = [0]+[1]*N
for i in range(1, K+1):
    if i==2: 
        for i in range(1, N+1):
            dp[2][i] = i+1
    else: dp[i][1] = i

for i in range(3, K+1):
    for j in range(2, N+1):
        dp[i][j] = dp[i][j-1]%1000000000+dp[i-1][j]%1000000000
print(dp[K][N]%1000000000)

