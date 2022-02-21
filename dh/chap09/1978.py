N = int(input())
nums = map(int, input().split())
cnt = 0
for i in nums:
    answer = True
    if i==1: answer = False
    else:
        for j in range(2, int(i**(1/2))+1):
            if i%j==0: answer = False
    if answer: cnt += 1
print(cnt)