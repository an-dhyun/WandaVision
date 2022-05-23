import sys

N = int(input()) 
W = [list(map(int, input().split())) for _ in range(N)]
min_value = sys.maxsize

def dfs(s, n, val, visited):
    global min_value
    if len(visited) == N:
        if W[n][s] != 0: # 마지막 장소에서 처음 장소로 갈 수 있어야 함
            min_value = min(min_value, val + W[n][s]) 
        return
    for i in range(N): 
        if W[n][i] != 0 and i not in visited and val < min_value: 
            visited.append(i) 
            dfs(s, i, val + W[n][i], visited)
            visited.pop()


for i in range(N):
    dfs(i, i, 0, [i])

print(min_value)