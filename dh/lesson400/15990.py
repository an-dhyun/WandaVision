import sys

max = 100000
mod = 1000000009

# 배열 초기화
dp = [[0]*4 for _ in range(max+1)]
dp[1] = [0,1,0,0]
dp[2] = [0,0,1,0]
dp[3] = [0,1,1,1]

# 배열 값 구하기 - 미리 안나누면 메모리 초과남
for i in range(4, max+1):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3])%mod
    dp[i][2] = (dp[i-2][1] + dp[i-2][3])%mod
    dp[i][3] = (dp[i-3][1] + dp[i-3][2])%mod

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(sum(dp[n])%mod)