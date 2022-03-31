import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [1]*N # 자기자신으로 구성될 수 있음
for i in range(1, N):
    for j in range(i):
        if A[i] < A[j]: # 이전의 원소가 자기보다 클 경우
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
