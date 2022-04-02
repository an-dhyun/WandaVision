import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
rev_A = A[::-1]

dp_up = [1 for _ in range(N)]
dp_down = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp_up[i] = max(dp_up[j]+1, dp_up[i])
        if rev_A[i] > rev_A[j]:
            dp_down[i] = max(dp_down[j]+1, dp_down[i])

result = [0 for i in range(N)]

for i in range(N):
    result[i] = dp_up[i] + dp_down[N-i-1] - 1
print(max(result))