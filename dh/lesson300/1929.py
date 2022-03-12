import sys
M, N = map(int, sys.stdin.readline().split())
nums = [True]*(N+1)
nums[0] = nums[1] = False

for i in range(2, int(N**(1/2))):
    for j in range(i+i, N+1, i):
        nums[j] = False

for i in range(M, N+1):
    if nums[i]: print(i)
