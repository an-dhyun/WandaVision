import sys
nums = [0]*100001

N = int(sys.stdin.readline())
for i in range(N):
    nums[int(sys.stdin.readline())] += 1

for i in range(len(nums)):
    for j in range(0, nums[i]):
        print(i)