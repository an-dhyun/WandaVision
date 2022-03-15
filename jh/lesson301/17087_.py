from sys import stdin
input = stdin.readline

n, s = map(int, input().split())
a = list(map(int, input().split()))
dif = list(set(abs(a[i]-s) for i in range(n)))
d = min(dif)

# Euclidean algorithm
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

for i in range(len(dif)):
    d = gcd(dif[i], d)

print(d)
