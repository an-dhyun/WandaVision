import sys
N, k = map(int, sys.stdin.readline().split())
q = [x for x in range(1, N+1)]
idx = 0; answer = []
for i in range(N):
    idx += k-1
    while True: 
        if idx >= len(q): idx -= len(q)
        else: break
    answer.append(q[idx])
    q.pop(idx)
print("<", end='')
for i in answer[:N-1]:
    print("%s, "%i, end='')
print("%s>"%(answer[N-1]))