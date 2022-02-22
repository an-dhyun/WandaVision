import sys

n = int(input())
list_num = []
for i in range(n):
    num = int(sys.stdin.readline())
    list_num.append(num)

for j in sorted(list_num):
    print(j)