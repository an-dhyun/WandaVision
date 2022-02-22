N, M = map(int, input().split())
nums = list(map(int, input().split()))
sums = []
for i in range(len(nums)-2):
    for j in range(i+1, len(nums)-1):
        for k in range(j+1, len(nums)):
            sums.append(nums[i] + nums[j] + nums[k])
sums_fin = []
for i in sums:
    if i < M: sums_fin.append(i)
print(max(sums_fin))