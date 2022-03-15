import sys
system = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N, B = map(str, sys.stdin.readline().split())
B = int(B)
N = list(N)
answer = 0
for i in range(len(N)-1, -1, -1):
    answer += (B**(len(N)-1-i)) * system.index(N[i])
print(answer)