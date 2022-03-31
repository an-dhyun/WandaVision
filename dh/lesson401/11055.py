import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [A[0]]+[0]*(N-1) # 첫번째 원소만 넣어놓음

for i in range(1, N):
    dp[i] = A[i] # dp 행렬을 0에서 지금 숫자로 세팅
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+A[i])
print(max(dp))