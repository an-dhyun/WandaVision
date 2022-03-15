import sys
input = sys.stdin.readline

n, b = map(int, input().split())

def solution(n, b):
    cnt = ''
    while n > 0:
        n, mod = divmod(n, b)
        if mod < 10:
            cnt += str(mod)
        else:
            cnt += chr(mod+55)
    return cnt[::-1]

print(solution(n, b))