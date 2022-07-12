import sys
N, K = map(int, sys.stdin.readline().split())
A = []
answer = 0

for _ in range(N):
    A.append(int(sys.stdin.readline()))

for i in range(N-1, -1, -1):
    if A[i]<=K: 
        answer += K//A[i]
        K -= A[i] * (K//A[i])
print(answer)