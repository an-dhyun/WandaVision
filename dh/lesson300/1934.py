import sys

def gcd(a, b):
    while a%b != 0:
        temp = a 
        a = b
        b = temp%b 
    return b

for _ in range(int(sys.stdin.readline())):
    A, B = map(int, sys.stdin.readline().split())
    if A>B:
        result = gcd(A, B)
    else:
        result = gcd(B, A)
    print(A*B/result)