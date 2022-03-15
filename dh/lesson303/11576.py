import sys
A, B = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

ten = 0; idx = 0
for i in range(m-1, -1, -1):
    ten += A**idx * nums[i]
    idx += 1
toB = ''

idx = 0
while ten:
    toB = str(ten%B) + " " + toB
    ten //= B
print(toB)