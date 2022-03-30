# < 방법 1 >
# dp : 각 자리별 합으로 나타낼 수 있는 제곱수의 최소값
# 1. 제곱수에 각각 1을 넣어주고
# 2. 각각 제곱수를 뺸 뒤 그 값을 이전 행렬에서 얻어와서 계산
# --> 이렇게 하면 제곱수끼리의 합 (ex. 16+16) 에서 예외 발생

# < 방법 2 >
# dp : 각 자리별 합으로 나타낼 수 있는 제곱수의 최소값
# 1. 제곱수를 미리 다 계산해주고
# 2. 이 숫자에서 각 제곱수를 빼주면서 최소값 계산

import sys

N = int(sys.stdin.readline())
nums = [i*i for i in range(1,317)]
dp = [0]*(N+1)

for i in range(1,N+1):
    sqs = []
    for j in nums:
        if j>i : break
        sqs.append(dp[i-j] + dp[j])
    dp[i] = min(sqs)+1

print(dp[N])