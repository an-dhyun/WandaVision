import sys
N = int(sys.stdin.readline())
d = [[0 for x in range(10)] for x in range(101)]
d[1] = [0] + [1]*9
for i in range(2, N+1):
    for j in range(10):
        if j==0: d[i][0] = d[i-1][1]
        elif j==9: d[i][9] = d[i-1][8]
        else:
            d[i][j] = d[i-1][j-1] + d[i-1][j+1]
print(sum(d[N]))
