import sys
input = sys.stdin.readline
from collections import deque

def bfs(v):
    visited[v] = 1
    q = deque()
    q.append(v)
    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                visited[i] = -visited[a]
                q.append(i)
            else:
                if visited[i] == visited[a]:
                    return False
    return True

for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    answer = 1
    
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1, v+1):
        if visited[i] == 0:
            if not bfs(i):
                answer = -1
                break

    print("YES" if answer == 1 else "NO")