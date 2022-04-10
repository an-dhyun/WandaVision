import sys
E, S, M = map(int, sys.stdin.readline().split())
E = E%15; S = S%28; M = M%19


answer = 1
while True:
    if (answer%15 == E) & (answer%28 == S) & (answer%19 == M):
        break
    else: answer += 1
print(answer)
