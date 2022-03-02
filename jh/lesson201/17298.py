import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
NGE = [-1] * N
stack = [0]

for i in range(1,N):
    # repeat if stack is not empty
    # repeat if A[top of stack] < A[i]
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()] = A[i]
    stack.append(i)

print(*NGE)