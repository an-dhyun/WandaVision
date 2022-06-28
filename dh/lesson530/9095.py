import sys
def cal(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return cal(n-1)+cal(n-2)+cal(n-3)

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    print(cal(n))
