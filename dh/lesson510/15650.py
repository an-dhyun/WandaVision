def dfs(n):
    if len(s)==M:
        print(' '.join(map(str, s)))
        return
    for i in range(n, N+1):
        if visited[i]: continue
        visited[i] = True
        s.append(i)
        dfs(i)
        s.pop()
        visited[i] = False


N, M = map(int, input().split())
s = []
visited = [False] * (N+1)

dfs(1) # 시작점을 설정해둬서 자기보다 작은 곳은 탐색하지 못하도록 설정