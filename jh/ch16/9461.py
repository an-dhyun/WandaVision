t = int(input())
dp = [0] * 101
dp[1], dp[2], dp[3] = 1, 1, 1
dp[4], dp[5], dp[6] = 2, 2, 3
dp[7], dp[8] = 4, 5
for i in range(9, 101):
    dp[i] = dp[i-1] + dp[i-5]

for i in range(t):
    print(dp[int(input())])