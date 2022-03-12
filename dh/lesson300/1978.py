import sys
total_num = [False]*1001

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))
for i in nums: total_num[i] = True
total_num[1] = False
for i in range(2, int(max(nums)**(1/2))+1):
    for j in range(2, 1001):
        if (i!=j) & (j%i==0): total_num[j] = False
print(total_num[:10])
print(sum(total_num))
