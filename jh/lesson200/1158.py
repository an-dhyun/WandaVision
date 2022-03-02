import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = [x for x in range(1, N+1)]
que = [] # remove
num = 0 # remove number

for _ in range(N):
    num += K-1
    if num >= len(numbers):
        num = num % len(numbers)
    que.append(str(numbers.pop(num))) # string for print

print("<"+", ".join(que)+">")