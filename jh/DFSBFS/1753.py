# 백준 - 바이러스

N = int(input()) # 컴퓨터 수
M = int(input()) # 쌍의 수

graph = [[] for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (N+1)

def dfs(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)

dfs(graph, 1, visited)
print(sum(visited)-1)
