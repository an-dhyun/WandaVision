# dp : 각 숫자 갯수별, 각 합별 나타낸 표 - K X N
import sys
N, K = map(int, sys.stdin.readline().split())
dp = [[0]*201 for _ in range(201)]
dp[1] = [1]*201 # 개수가 한개일 땐 무조건 1가지

for i in range(201):
    dp[2][i] = i+1 # 개수가 두개일 땐 무조건 i+1가지

for i in range(2, 201): # K iteration
    dp[i][1] = i # i개 합으로 1을 만들려면 i가지경우밖에없음
    for j in range(2, 201): # N iteration
        dp[i][j] = (dp[i][j-1]+dp[i-1][j]) % 1000000000 # 점화식

print(dp[K][N])