def fact(a, b):
    answer = 1
    for i in range(a, b, -1):
        answer *= i
    return answer

import sys

n, m = map(int, sys.stdin.readline().split())
answer = fact(n, m)/fact(n-m, 0)
cnt = 0
for i in range(len(str(answer))-1, -1, -1):
    if str(answer)[i]==0: cnt += 1
    else: break
print(cnt)