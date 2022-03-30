import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = [1]*N

for i in range(1, N):
    for j in range(i):
        if A[i]>A[j]: dp[i] = max(dp[j]+1, dp[i])
max_ord = max(dp)
print(max_ord)

lst = []
for i in range(N-1, -1, -1):
    if dp[i] == max_ord:
        lst.append(str(A[i]))
        max_ord -= 1
lst.reverse()

print(' '.join(lst))