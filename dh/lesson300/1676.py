import sys
N = int(sys.stdin.readline())
fact = 1
for i in range(2, N+1):
    fact *= i
nums = list(str(fact))
cnt = 0
for i in range(len(nums)-1, -1, -1):
    if nums[i]=='0': cnt += 1
    else: break
print(cnt)