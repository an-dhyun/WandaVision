import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))
new_A = [0]*1000000
for i in A:
    new_A[i-1] += 1

stack = []
answer = [-1] * N
stack.append(0)

for i in range(1, N):
    while stack and new_A[A[stack[-1]]-1] < new_A[A[i]-1]:
        answer[stack.pop()] = A[i]
    stack.append(i)
    
answer = list(map(str, answer))
print(" ".join(answer))