def dfs(n):
    if len(s)==M:
        print(' '.join(map(str, s)))
        return
    for i in range(n, N+1):
        visited[i] = True
        s.append(i)
        dfs(i)
        s.pop()
        visited[i] = False

N, M = map(int, input().split())
s = []
visited = [False] * (N+1)
dfs(1)