import sys
S = list(sys.stdin.readline().strip())
for i in range(97, 123):
    print(S.count(chr(i)), end=' ')