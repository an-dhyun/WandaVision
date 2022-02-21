M = int(input())
N = int(input())

nums = [True]*(N+1)
nums[0] = nums[1] = False
for i in range(M): nums[i] = False

for i in range(2, int(N**(1/2))+1):
    for j in range(i+i, N+1, i):
        nums[j] = False

if sum(nums)==0: print(-1)
else:
    sum = 0
    for i in range(M, N+1):
        if nums[i]: sum += i
    print(sum)
    print(nums.index(True))