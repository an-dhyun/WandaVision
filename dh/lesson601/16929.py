import sys

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    lst = list(sys.stdin.readline().rstrip())
    graph.append(lst)

answer = True
visited = [[False]*M for _ in range(N)]
dx = [1, -1, 0, 0] # 사방으로만 이동 가능
dy = [0, 0, 1, -1]

answer = False
def dfs(x, y, depth):
    print(x, y)
    if depth >= 4: 
        print("Yes")
        exit()
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M and graph[nx][ny]==graph[x][y]:
            if (depth==3 and visited[nx][ny]) or (not visited[nx][ny]): dfs(nx, ny, depth+1)                

for i in range(N):
    for j in range(M):
        if not visited[i][j]: dfs(i, j, 0)
print("No")