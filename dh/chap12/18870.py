import sys
N = int(sys.stdin.readline())
inputs = list(map(int, sys.stdin.readline().split()))
if min(inputs)<0: 
    nums = [False]*(max(inputs)+abs(min(inputs))+1)
    for i in inputs:
        nums[i+abs(min(inputs))] = True
    for i in inputs:
        print(sum(nums[:i+abs(min(inputs))]), end=' ')
else:
    nums = [False]*(max(inputs)+1)
    for i in inputs:
        nums[i] = True
    for i in inputs:
        print(sum(nums[:i]), end=' ')