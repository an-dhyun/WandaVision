import sys
N = int(sys.stdin.readline())
A = [0] + list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(N+1)] # 전부 각각의 시점에서 하나의 수열을 만들수 있음

for i in range(2, N+1):
    for j in range(1, i):
        if A[i] > A[j]: # 커질때만 고려해야함
            dp[i] = max(dp[j]+1, dp[i]) # 최적의 수열을 고려해야함

print(max(dp))