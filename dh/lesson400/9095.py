import sys
T = int(sys.stdin.readline())
d = [0]*12
d[0] = 1; d[1] = 2; d[2] = 4

for i in range(3,12):
    d[i] = sum(d[i-3:i])

for i in range(T):
    n = int(sys.stdin.readline())
    print(d[n-1])