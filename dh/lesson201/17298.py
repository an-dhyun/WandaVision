import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))
stack = []
answer = [-1]*N
stack.append(0)

for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

answer = list(map(str, answer))
print(" ".join(answer))