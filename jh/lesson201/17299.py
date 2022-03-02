import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)

NGF = [-1] * N
stack = [0]

for i in range(1,N):
    # repeat if stack is not empty'
    # repeat if A[top of stack] < A[i]
    while stack and cnt[A[stack[-1]]] < cnt[A[i]]:
        NGF[stack.pop()] = A[i]
    stack.append(i)

print(*NGF)