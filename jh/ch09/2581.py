m = int(input())
n = int(input())
prime = []

for i in range(m, n+1):
    tmp = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                tmp += 1
        if prime == 0:
            prime.append(i)

sum_prime = sum(prime)
if sum_prime > 0:
    print(sum_prime)
    print(min(prime))
else:
    print(-1)