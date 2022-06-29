### DFS ###

n = int(input())
visit = [False] * n
graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(depth, idx):
    global answer
    if depth == n//2:
        a, b = 0, 0 # start, link team
        for i in range(n):
            for j in range(i+1, n):
                if visit[i] and visit[j]:
                    a += (graph[i][j] + graph[j][i])
                elif not visit[i] and not visit[j]:
                    b += (graph[i][j] + graph[j][i])
        answer = min(answer, abs(a-b))
        return
    
    for i in range(idx, n):
        if not visit[i]:
            visit[i] = True
            dfs(depth+1, i+1)
            visit[i] = False

answer = float('Inf')
dfs(0, 0)
print(answer)