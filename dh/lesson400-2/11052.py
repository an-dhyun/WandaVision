import sys
N = int(sys.stdin.readline())
P = [0] + list(map(int, sys.stdin.readline().split()))

dp = [0]*(N+1) # n개 살때 최대값
dp[1] = P[1] # 한개 살때는 무조건 P[0]
for i in range(2, N+1): # 2개 살때부터는
    dp[i] = P[i] # 2개들이 팩을 산다고 가정하고 
    for j in range(i):
        dp[i] = max(dp[i-j]+P[j], dp[i]) # 계속 i-j + j 사는것과 비교

print(dp[N])