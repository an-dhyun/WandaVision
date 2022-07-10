from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
que = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            que.append([i, j])

def bfs():
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                que.append([nx, ny])

bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(i))

print(answer - 1)