t = int(input())

def isPrime(num):
    if num ==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

for i in range(t):
    n = int(input())
    a = int(n/2)
    b = int(n/2)
    for j in range(int(n/2)):
        if isPrime(a) & isPrime(b):
            print(a, b)
            break
        else:
            a = a-1
            b = b+1