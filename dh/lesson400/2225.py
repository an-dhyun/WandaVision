import sys
N, K = map(int, sys.stdin.readline().split())
dp = [[0]*201 for _ in range(201)] # K x N으로 참조할 행렬

# 미리 세팅
for i in range(201):
    dp[1][i] = 1 # K = 1일 경우 한가지뿐
    dp[2][i] = i+1 # K = 2일 경우 (자기자신 + 1)가지 뿐

for i in range(2, 201):
    dp[i][1] = i # N = 1일 경우 K가지 뿐
    for j in range(2, 201):
        dp[i][j] = (dp[i][j-1]+dp[i-1][j]) % 1000000000 # 점화식

print(dp[K][N])