import sys
N = int(sys.stdin.readline())
P = [0] + list(map(int, sys.stdin.readline().split()))

dp = [0]*(N+1)
dp[1] = P[1]

for i in range(2, N+1):
    dp[i] = P[i]
    for j in range(i):
        dp[i] = min(dp[i-j]+P[j], dp[i]) # 최소값이므로 min으로 변경

print(dp[N])