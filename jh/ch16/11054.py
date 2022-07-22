N = int(input())
A = list(map(int, input().split()))
dpi = [1] * N # increase
dpd = [1] * N # decrease
dp = [0] * N # sum

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dpi[i] = max(dpi[j]+1, dpi[i])

for i in range(N-2, -1, -1):
    for j in range(N-1, i, -1):
        if A[i] > A[j]:
            dpd[i] = max(dpd[j]+1, dpd[i])

for i in range(N):
    dp[i] = dpi[i] + dpd[i] - 1

print(max(dp))