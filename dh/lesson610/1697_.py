import sys
import collections 


count = 0

def bfs():
    q = collections.deque()
    q.append(N)
    while q:
        n = q.popleft()
        if n==K: 
            print(dist[n])
            break
        for new_n in (n-1, n+1, n*2):
            if 0 <= new_n <= MAX and not dist[new_n]:
                dist[new_n] = dist[n] + 1
                q.append(new_n)

N, K = map(int, sys.stdin.readline().split())
MAX = 10 ** 5
dist = [0] * (MAX + 1)
bfs()