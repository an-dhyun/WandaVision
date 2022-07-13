import sys
N = int(sys.stdin.readline())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline()))
nums.sort()
for i in nums:
    print(i)