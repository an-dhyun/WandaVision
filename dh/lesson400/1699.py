import sys
N = int(sys.stdin.readline())
square = [i*i for i in range(1, 317)] # 시간 절약을 위해 제곱값 미리 계싼
dp = [0]*(N+1)

for i in range(1, N+1): # N까지 반복
    sqs = []
    for j in square:
        if j>i: break
        sqs.append(dp[i-j])
    dp[i] = min(sqs) + 1

print(dp[N])