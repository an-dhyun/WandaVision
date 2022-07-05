from collections import deque
import sys

# 그래프 작성
N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b); graph[a].sort()
    graph[b].append(a); graph[b].sort()

# dfs
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
visited = [False] * (N+1) # visited 초기화
dfs(graph, V, visited)
print()

# bfs
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True # 탐색 시작 노드를 큐에 삽입하고 방문 처리
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
visited = [False] * (N+1)
bfs(graph, V, visited)
print()

