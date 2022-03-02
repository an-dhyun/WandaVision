def isPrime(num):
    if num ==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

all_num = [x for x in range(123456*2+1)]
prime = []

for i in all_num:
    if isPrime(i):
        prime.append(i)

while True:
    n = int(input())
    if n == 0:
        break
    else:
        cnt = 0
        for i in prime:
            if n < i <= 2*n:
                cnt += 1
        print(cnt)