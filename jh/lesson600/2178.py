import sys
import collections

n, m = map(int, input().split())
graph = [list(map(int, ' '.join(input()).split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

que = collections.deque([(0, 0)])
answer = 0

while que:
    x, y = que.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx, ny))

print(graph[n-1][m-1])