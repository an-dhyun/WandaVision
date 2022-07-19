n = int(input())
A = [0] * 10001
for i in range(1, n+1):
    A[i] = int(input())
dp = [0] * (10001)
dp[1] = A[1]
dp[2] = A[1] + A[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-1], A[i]+A[i-1]+dp[i-3], A[i]+dp[i-2])

print(dp[n])