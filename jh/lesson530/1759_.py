### back tracking ###

from itertools import combinations

l, c = map(int, input().split())
arr = sorted(list(input().split()))

com = combinations(arr, l)

for i in com:
    cnt = 0
    for j in i:
        if j in 'aeiou':
            cnt += 1
    if (cnt >= 1) and (cnt <= l-2):
        print(''.join(i))