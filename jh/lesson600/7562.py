import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(sx, sy, ax, ay):
    q = deque()
    q.append([sx, sy])
    graph[sx][sy] = 1

    while q:
        a, b = q.popleft()
        if a == ax and b == ay:
            print(graph[ax][ay] - 1)
            return
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < l and 0 <= y < l and graph[x][y] == 0:
                q.append([x, y])
                graph[x][y] = graph[a][b] + 1

t = int(input())
for i in range(t):
    l = int(input())
    sx, sy = map(int, input().split())
    ax, ay = map(int, input().split())
    graph = [[0] * l for i in range(l)]
    bfs(sx, sy, ax, ay)