import sys

T = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(T)]
m = max(nums)

prime = [True]*(m+1)
prime[0] = prime[1] = False
for i in range(2, int(m**0.5)+1):
    if prime[i]:
        for j in range(i+i, m+1, i): 
            if prime[j]: prime[j] = False

for num in nums:
    cnt = 0
    for i in range(int(num//2), num-2):
        if prime[i] and prime[num-i]:
            cnt += 1
    print(cnt)
