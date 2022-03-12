import sys
N = int(sys.stdin.readline())
answer = 1
for i in range(2, N+1):
    answer *= i
print(answer)
