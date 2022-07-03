# # 참고 : https://kyun2da.github.io/2020/09/21/ABCDE/
# N명의 사람 중 일직선 방향으로 친구관계가 성립하는 다섯명이 있기만 하면 됨
# import sys

# n, m = map(int, input().split())
# arr = [[] for _ in range(n)]
# visited = [False] * n

# # 그래프를 인접 리스트* 방식으로 표현
# # *인접 리스트 : 각각의 노드에 연결된 노드들을 원소로 갖는 리스트들의 배열
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     arr[a].append(b)
#     arr[b].append(a)


# def dfs(idx, number):
#     if number == 4: # 그래프의 깊이가 5로 판단되면
#         print(1)
#         exit()
#     for i in arr[idx]: # 해당 노드와 연결된 모든 노드에 대하여 반복
#         if not visited[i]:
#             visited[i] = True
#             dfs(i, number + 1)
#             visited[i] = False

# # 노드를 순서대로 방문하며 dfs를 수행
# for i in range(n): # 각각의 노드에 대하여 반복
#     visited[i] = True
#     dfs(i, 0)
#     visited[i] = False

# print(0)

# 복습용
import sys
N, M = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N)]
visited = [False] * N

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(idx, number):
    # if sum(visited) == 5: -> 시간초과남!
    if number == 4:
        print(1)
        exit()
    for i in arr[idx]:
        if visited[i] == False:
            visited[i] = True
            dfs(i, number + 1)
            visited[i] = False

for i in range(N):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)