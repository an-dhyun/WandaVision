import sys
from collections import Counter
n = int(sys.stdin.readline())
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline()))
numbers.sort()

print(round(sum(numbers)/n)) # mean
print(numbers[n//2])# median
# mode
cnt = sorted(Counter(numbers).items(), key = lambda x: (-x[1], x[0]))
if n == 1:
    print(numbers[0])
else:
    if cnt[0][1] != cnt[1][1]:
        print(cnt[0][0])
    else:
        print(cnt[1][0])
print(max(numbers)-min(numbers)) # range
