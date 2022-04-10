import sys
N, M = map(int, sys.stdin.readline().split())
vals = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
print(vals)