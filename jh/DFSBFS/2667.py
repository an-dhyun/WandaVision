# 백준 - 단지번호붙이기
from collections import deque

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count

answer = [bfs(graph, i, j) for i in range(N) for j in range(N) if graph[i][j] == 1]
answer.sort()
print(len(answer))

for i in answer:
    print(i)