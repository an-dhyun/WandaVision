import sys

nums = [True]*1000001
nums[0]=nums[1] = False
for i in range(2, int(1000000**(1/2))+1):
    for j in range(i+i, 1000001, i):
        nums[j] = False

while True:
    n = int(sys.stdin.readline())
    if n==0: break
    answer = -1
    for i in range(n-2, n//2-1, -1):
        if nums[i]*nums[n-i]==1: 
            answer = i
            break
    if answer==-1: print("Goldbach's conjecture is wrong.")
    else: print("%s = %s + %s"%(n, n-answer, answer))