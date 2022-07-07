from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

def bfs(g, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    que = deque()
    que.append((x, y))
    g[x][y] = 0 # 재방문 x
    cnt = 1

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if g[nx][ny] == 1:
                g[nx][ny] = 0
                que.append((nx, ny))
                cnt += 1
    return cnt

answer = [bfs(graph, i, j) for i in range(n) for j in range(n) if graph[i][j] == 1]
answer.sort()
print(len(answer))

for i in answer:
    print(i)