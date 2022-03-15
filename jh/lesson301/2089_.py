import sys
input = sys.stdin.readline

n = int(input())
cnt = ''
if n == 0:
    print(0)
else:
    while n != 0:
        if n % (-2) != 0:
            cnt = '1' + cnt
            n = n//-2 + 1
        else:
            cnt = '0' + cnt
            n //= -2

print(cnt)