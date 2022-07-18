### 쉬운 계단 수 ###

N = int(input())
dp = [[0] * 10 for _ in range(N+1)]
dp[1] = [0] + [1 for _ in range(1, 10)]

for i in range(2, N+1):
    for j in range(0, 10): # 맨끝에 오는 숫자
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N])%1000000000)
