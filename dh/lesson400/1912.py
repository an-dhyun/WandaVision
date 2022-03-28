import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))
sums = [nums[0]]
dp = [0] * n

for i in range(1,n):
    sums.append(max(nums[i], sums[i-1]+nums[i]))

print(max(sums))