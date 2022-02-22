N = int(input())
result = 0
for i in range(N):
    nums = list(map(int, str(i)))
    if sum(nums)+i == N: 
        result = i
        break
print(result)