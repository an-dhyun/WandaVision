N, K = map(int, input().split())
W = [0]
V = [0]
for i in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)
dp=[[0]*(K+1) for _ in range(N+1)]

for i in range(N+1):
    for w in range(K+1):
        if W[i] <= w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-W[i]]+V[i])
        else:
            dp[i][w] = dp[i-1][w]

print(dp[-1][-1])