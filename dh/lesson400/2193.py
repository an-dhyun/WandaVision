import sys
N = int(sys.stdin.readline())
d = [0]*N
if N==1: print(1)
else:
    d[0] = d[1] = 1
    for i in range(2, N):
        d[i] = d[i-1] + d[i-2]
    print(d[N-1])
