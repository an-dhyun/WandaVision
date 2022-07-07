import sys
sys.setrecursionlimit(1000)

def dfs(x, y): # x행 y열의 원소를 방문
    global count   
    visited[x][y] = True # 방문처리
    # 값이 존재하고, 방문하지 않았고, 집이 있을 경우 집계 및 이동
    if (x > 0) and (visited[x-1][y]==False) and (graph[x-1][y]==1):
        count += 1
        dfs(x-1, y)
    if (y > 0) and (visited[x][y-1]==False) and (graph[x][y-1]==1):
        count += 1
        dfs(x, y-1)
    if (x < N-1) and (visited[x+1][y]==False) and (graph[x+1][y]==1): 
        count += 1
        dfs(x+1, y)
    if (y < N-1) and (visited[x][y+1]==False) and (graph[x][y+1]==1): 
        count += 1
        dfs(x, y+1)
        
N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    lst = list(map(int, list(sys.stdin.readline().rstrip())))
    graph.append(lst)

visited = [[False] * N for _ in range(N)]
counts = []
for i in range(N):
    for j in range(N):
        # 집이 있고 방문하지 않은 경우에만
        if (graph[i][j]==1) and (not visited[i][j]): 
            count = 1
            dfs(i, j)
            counts.append(count)

counts.sort()
print(len(counts))
for i in counts: print(i)