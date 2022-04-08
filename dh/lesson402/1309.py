import sys
N = int(sys.stdin.readline())
dp = [[0 for _ in range(3)] for _ in range(N)]
# 설치 x, 왼쪽에 설치, 오른쪽에 설치
dp[0] = [1,1,1]
for i in range(1, N):
    dp[i][0] = (dp[i-1][0]+dp[i-1][1]+dp[i-1][2])%9901
    dp[i][1] = (dp[i-1][0]+dp[i-1][2])%9901
    dp[i][2] = (dp[i-1][0]+dp[i-1][1])%9901

print(sum(dp[N-1])%9901)