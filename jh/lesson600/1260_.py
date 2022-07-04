n, m, v = map(int, input().split())

mat = [[0] * (n+1) for i in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    a, b = map(int, input(). split())
    mat[a][b] = mat[b][a] = 1

def dfs(v):
    visited[v] = 1
    print(v, end = ' ')
    for i in range(1, n+1):
        if (mat[v][i] == 1 and visited[i] == 0):
            dfs(i)

def bfs(v):
    que = [v]
    visited[v] = 0
    while que:
        v = que.pop(0)
        print(v, end = ' ')
        for i in range(1, n+1):
            if (mat[v][i] == 1 and visited[i] == 1):
                que.append(i)
                visited[i] = 0

dfs(v)
print()
bfs(v)