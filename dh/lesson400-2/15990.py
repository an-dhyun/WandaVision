import sys

max = 100001
mod = 1000000009

# 시간 절약을 위해 행렬 미리 계산
dp = [[0]*4 for _ in range(max)]
dp[1] = [0,1,0,0]
dp[2] = [0,0,1,0]
dp[3] = [0,1,1,1]

for i in range(4, max):
    # 1. 숫자셋이 1로 끝나려면 이전 숫자셋이 2 또는 3으로 끝나야함
    dp[i][1] = (dp[i-1][2] + dp[i-1][3])%mod
    # 2. 숫자셋이 2로 끝나려면 이전 숫자셋이 1 또는 3으로 끝나야함
    dp[i][2] = (dp[i-2][1] + dp[i-2][3])%mod
    # 3. 숫자셋이 3으로 끝나려면 이전 숫자셋이 1 또는 2로 끝나야함
    dp[i][3] = (dp[i-3][1] + dp[i-3][2])%mod

# 정답 출력
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(sum(dp[n])%mod)