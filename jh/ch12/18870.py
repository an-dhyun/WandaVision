import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
numbers2 = sorted(list(set(numbers)))

dic = {numbers2[i] : i for i in range(len(numbers2))}
for i in numbers:
    print(dic[i], end=" ")