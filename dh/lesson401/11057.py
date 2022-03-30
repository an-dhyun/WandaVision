import sys
N = int(sys.stdin.readline())
dp = [[0 for _ in range(10)] for _ in range(1001)]
dp[1] = [1]*10 # 한자리는 모두 경우의 수가 하나

for i in range(2, N+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][:j+1])
        
print(sum(dp[N])%10007)