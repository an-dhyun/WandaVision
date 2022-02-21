nums = [True]*((123456*2)+1)
nums[0]=nums[1]=False
for i in range(2, int((123456*2)**(1/2))+1):
    for j in range(i+i, (123456*2)+1, i): 
        nums[j] = False
    

while True:
    n = int(input())
    if n==0: break
    print(sum(nums[n+1:2*n+1]))