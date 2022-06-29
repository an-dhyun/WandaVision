### DFS ###

n = int(input())
visit = [False] * n
graph = [list(map(int, input().split())) for _ in range(n)]

def dfs():
    global answer
    a, b = 0, 0 # start, link team
    for i in range(n):
        for j in range(i+1, n):
            if visit[i] and visit[j]:
                a += (graph[i][j] + graph[j][i])
            elif not visit[i] and not visit[j]:
                b += (graph[i][j] + graph[j][i])
    answer = min(answer, abs(a-b))
    return

def resolve(iter):
    if iter == n:
        dfs()
        return
    visit[iter] = True
    resolve(iter+1)
    visit[iter] = False
    resolve(iter+1)

answer = float('Inf')
resolve(0)
print(answer)