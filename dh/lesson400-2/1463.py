import sys
N = int(sys.stdin.readline())
dp = [0]*(N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1]+1

    if i%2==0: # 2로 나누어떨어질 경우 - 1뺀거랑 2나눈거랑 비교
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3==0: # 3으로 나누어떨어질경우 - 1뺀거랑 3나눈거랑 비교
        dp[i] = min(dp[i], dp[i//3]+1)
    
    # 2와 3 둘다 나누어떨어질 수 있고, 순서에 따라 달라질 수 있으므로 모든 경우 고려

print(dp[N])