import sys
input = sys.stdin.readline

# sieve of Eratosthenes
num = [x for x in range(1000001)]
for i in range(2, 1001):
    if num[i]:
        for j in range(2*i, 1000001, i):
            num[j] = False

while True:
    n = int(input())

    if n == 0:
        break
    
    for i in range(3, len(num)):
        if num[i] and num[n-i]:
            print(n, '=', i, '+', n-i)
            break