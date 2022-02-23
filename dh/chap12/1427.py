import sys
N = int(sys.stdin.readline())
nums = list(map(int, str(N)))
nums.sort(reverse=True)
for i in nums: print(i, end='')