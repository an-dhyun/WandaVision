import sys
T = int(sys.stdin.readline())

for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().strip().split())
    k = 0
    for i in range(40001):
        