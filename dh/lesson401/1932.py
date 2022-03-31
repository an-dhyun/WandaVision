import sys
n = int(sys.stdin.readline())
nums = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(nums[i])):
        if j==0: # 맨 왼쪽일 경우
            nums[i][j] += nums[i-1][j]
        elif j==len(nums[i])-1: # 맨 오른쪽일 경우
            nums[i][j] += nums[i-1][j-1]
        else:
            nums[i][j] += max(nums[i-1][j], nums[i-1][j-1])


print(max(nums[n-1]))