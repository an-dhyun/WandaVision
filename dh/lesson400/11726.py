import sys
N = int(sys.stdin.readline())
d = [0]*(N+1)
d[0] = 1; d[1] = 2
for i in range(2, N+1):
    d[i] = d[i-2] + d[i-1]
    print(d)
print(d[N-1])