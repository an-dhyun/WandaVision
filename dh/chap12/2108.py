import sys
N = int(sys.stdin.readline())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline()))
# 1. 산술평균
print(round(sum(nums)/len(nums)))

# 2. 중앙값
nums.sort()
place = (N-1)/2
print(nums[int(place)])

# 3. 최빈값
whole = [0]*8001
for i in nums: whole[i+4000] += 1
mosts = []
for i in range(len(whole)):
    if whole[i]==max(whole): mosts.append(i-4000)
if len(mosts)==1: print(mosts)
else: 
    mosts.remove(min(mosts))
    print(min(mosts))

# 4. 범위
print(max(nums)-min(nums))