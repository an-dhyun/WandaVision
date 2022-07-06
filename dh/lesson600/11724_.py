# import sys
# sys.setrecursionlimit(5000)

# # 계속 깊이우선 탐색
# def dfs(idx, depth):
#     visited[idx] = True
#     for i in graph[idx]:
#         if not visited[i]:
#             dfs(i, depth + 1)

# N, M = map(int, sys.stdin.readline().split())
# graph = [[] for _ in range(N+1)]
# for _ in range(M):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)

# visited = [False] * (N+1)
# count = 0

# for i in range(1, N+1): # 1번부터 N번째 노드까지에 대해 순차적으로 탐색
#     if not visited[i]: # 만약 방문하지 않은 노드면
#         if not graph[i]: # 만약 연결된 노드가 없다면
#             count += 1 # 그 한개 자체로도 연결 요소가 될 수 있으므로 개수 세주기
#             visited[i] = True # 방문 처리
#         else: # 만약 연결된 노드가 있다면
#             dfs(i, 0) # 탐색 진행 -> 해당 노드와 연결된 노드는 모드 방문처리 되므로 그 노드에서 dfs를 시작할 수 없음
#             count += 1 # 카운트
# print(count)

# 복습
import sys
sys.setrecursionlimit(5000)

def dfs(idx, depth):
    visited[idx] = True
    for i in graph[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
count = 0
for i in range(1, N+1):
    if not visited[i]: # <--- 이걸 해줘야함
        if not graph[i]: # 연결된게 없으면
            count += 1
        else:
            dfs(i, 0)
            count += 1
print(count)
