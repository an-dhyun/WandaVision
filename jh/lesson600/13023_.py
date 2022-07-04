### dfs ###

n, m = map(int, input().split())
arr = [[] for i in range(n)]
visited = [False] * n

# 인접 리스트
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(idx, num):
    if num == 4:
        print(1)
        exit()
    for i in arr[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, num+1)
            visited[i] = False

for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)