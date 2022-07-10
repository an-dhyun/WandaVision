# import sys
# import collections

# M, N = map(int, sys.stdin.readline().split())
# tomatos = []
# for _ in range(N):
#     lst = list(map(int, sys.stdin.readline().rstrip().split()))
#     tomatos.append(lst)

# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1, -1]
# count = 0

# for i in tomatos: # 시작 당시 안익은 토마토 개수 세기
#     if 0 in i:
#         count += 1
# if count==0: # 모든 토마토가 다 익어있는 경우
#     print(0)
#     exit()

# def dfs(x, y, depth):
#     global result, count
#     result = depth
#     print(x, y)
#     if tomatos[x][y]==1: # 익은 토마토일 경우
#         for i in dx:
#             for j in dy:
#                 nx = x + i; ny = y + j
#                 if 0<=nx<N and 0<=ny<M and tomatos[nx][ny]==0: # 주변에 안익은 토마토가 있으면
#                     tomatos[nx][ny]==1 # 익게 하고
#                     count -= 1
#                     dfs(nx, ny, depth+1) # 다음 토마토로 넘어감

# result = 0
# for i in range(N):
#     for j in range(M):
#         dfs(i, j, 0)
# print(count)
# if count != 0: print(-1)
# else: print(result)

from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)