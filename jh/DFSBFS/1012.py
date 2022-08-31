# 백준 - 유기농 배추
from collections import deque

T = int(input())

def bfs(graph, x, y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 0
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                count += 1
    print(count)
