nums = [True]*10001
nums[0] = nums[1] = False
for i in range(2, 101):
    for j in range(i+i, 10001, i):
        nums[j] = False

T = int(input())
for i in range(T):
    n = int(input())
    n_nums = nums[:n]
    for i in range(int(n/2), 1, -1):
        if n_nums[i] and n_nums[n-i]: 
            print(i, n-i)
            break