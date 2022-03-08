import sys
input = sys.stdin.readline

s = list(input().rstrip())
tail = []

for i in range(len(s)):
    tail.append(s[i:])

tail.sort()

for i in tail:
    print(''.join(i))