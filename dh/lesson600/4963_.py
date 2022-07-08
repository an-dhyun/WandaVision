import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    # visited[x][y] = True # 방문처리

    dx = [1, 1, -1, -1, 1, -1, 0, 0] # 모든 경우를 이렇게 리스트로 넣어놔도 되는듯
    dy = [0, 1, 0, 1, -1, -1, 1, -1]
    graph[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
            dfs(nx, ny)

    # for i in range(x-1, x+2):
    #     for j in range(y-1, y+2):
    #         if (0<=i<h) and (0<=j<w) and graph[i][j]==1: 
    #             dfs(i, j) # 주변 다른 노드 탐색

while True:
    global visited, graph
    w, h = map(int, sys.stdin.readline().split())
    if w==0 and h==0: break # 종료조건
    graph = []
    for _ in range(h):
        inp = list(map(int, sys.stdin.readline().split()))
        graph.append(inp)
    # visited = [[False] * w for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            # if (not visited[i][j]) and (graph[i][j]==1):
            if graph[i][j]==1:
                dfs(i, j)
                count += 1
    print(count)

