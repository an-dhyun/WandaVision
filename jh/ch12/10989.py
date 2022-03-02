import sys

# counting sort
list_cnt = [0 for x in range(10001)]
n = int(sys.stdin.readline())

for i in range(n):
    num = int(sys.stdin.readline())
    list_cnt[num] += 1

for i in range(1, 10001):
    cnt = list_cnt[i]
    for j in range(cnt):
        print(i)