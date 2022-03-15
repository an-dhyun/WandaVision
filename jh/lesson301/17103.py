import sys
input = sys.stdin.readline

# sieve of Eratosthenes
num = [x for x in range(1000001)]
for i in range(2, 1001):
    if num[i]:
        for j in range(2*i, 1000001, i):
            num[j] = False


t = int(input())
for i in range(t):
    n = int(input())
    cnt = 0
    for j in range(2,n//2+1):
        if num[j] and num[n-j]:
            cnt += 1
    print(cnt)