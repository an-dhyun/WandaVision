import sys
n = int(sys.stdin.readline())
s = []
for _ in range(n):
    s.append(sys.stdin.readline().strip())
ss = list(set(s))
ss.sort()
ss.sort(key = len)
for i in ss:
    print(i)
