from sys import stdin
input = stdin.readline

t = int(input())

# Euclidean algorithm
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

for i in range(t):
    num = list(map(int, input().split()))
    num.pop(0) # remove case number
    sum = 0
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            sum += gcd(num[i], num[j])
    print(sum)