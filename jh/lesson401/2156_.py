import sys
input = sys.stdin.readline

n = int(input())
w = [0]
dp = [0]

for i in range(n):
    w.append(int(input()))

dp.append(w[1])
if n>1:
    dp.append(w[1]+w[2])
for i in range(3, n+1):
    dp.append(max(dp[i-1], dp[i-2]+w[i], dp[i-3]+w[i-1]+w[i]))
print(dp[n])