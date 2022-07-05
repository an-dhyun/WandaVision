import sys
sys.setrecursionlimit(10000) # 최대 재귀 횟수 제한 제거
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if visited[i] == 0:
        cnt += 1
        dfs(i)

print(cnt)