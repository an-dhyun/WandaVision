import sys
system = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N, B = map(int, sys.stdin.readline().split())
answer = ''

while N:
    answer += str(system[N%B])
    N //= B

print(answer[::-1])