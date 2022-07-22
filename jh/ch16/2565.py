N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]
C.sort(key = lambda x : x[0])
dp = [1] * N
for i in range(1, N):
    for j in range(0, i):
        if C[j][1] < C[i][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(N-max(dp))