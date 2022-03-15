a, b = map(int, input().split())
m = int(input())
arr = list(map(int,input().split()))[::-1]

# a -> 10
numA = 0
for i in range(m):
    numA += arr[i] * (a ** i)

# 10 -> b
result = []
while numA != 0:
    result.append(numA % b)
    numA //= b

for i in result[::-1]:
    print(i, end=' ')
