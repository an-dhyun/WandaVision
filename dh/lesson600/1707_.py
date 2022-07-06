# import sys
# def chk(idx, graph): # 이분 그래프인지 확인
#     answer = "YES"
#     if graph[idx]: # 비어있으면 참으로 출력, 아닐 경우
#         for i in graph[idx]:
#             graph[idx].remove(i) # 간선 하나 제거하고
#             # 부분요소가 2개 이상인지 확인
            
#     return answer

# K = int(sys.stdin.readline())
# for  _ in range(K):
#     V, E = map(int, sys.stdin.readline().split())
#     graph = [[] for _ in range(V+1)]
#     for _ in range(E):
#         u, v = map(int, sys.stdin.readline().split())
#         graph[u].append(v)
#         graph[v].append(u)
#     answer = "YES"
#     for i in range(1, V+1):
#         answer = chk(i, graph)
#     print(answer)

# # https://hongcoding.tistory.com/20
# import sys
# from collections import deque
# input = sys.stdin.readline

# def bfs(start, group):
#     queue = deque([start])  # 시작 정점 값을 큐에 담는다.
#     visited[start] = group  # 시작 정점 그룹을 설정
#     while queue:  # 큐가 존재할때까지 돈다.
#         x = queue.popleft()  # 큐의 맨앞 원소를 빼낸다.
#         # 상위 정점 : x, 하위 정점 : i
#         for i in graph[x]:  # 해당 정점에서 갈 수 있는 하위 정점들을 돈다.
#             if not visited[i]:  # 만약 그 하위 정점을 아직 방문하지 않았다면
#                 queue.append(i)  # 그 하위 정점을 큐에 추가하고
#                 visited[i] = -1 * visited[x]  # 상위 정점과 하위 정점을 다른 그룹으로 편성
#             elif visited[i] == visited[x]:  # 만약 하위 정점을 이미 방문했었는데, 상위 정점과 같은 그룹이라면
#                 return False  # False를 바로 리턴
#     return True  # 위의 조건에 걸리지 않았다면 True를 리턴


# for _ in range(int(input())):
#     V, E = map(int, input().split())
#     graph = [[] for i in range(V + 1)]  # 빈 그래프 생성
#     visited = [False] * (V + 1)  # 방문한 정점 체크
#     for _ in range(E):
#         a, b = map(int, input().split())
#         graph[a].append(b)  # 무방향 그래프
#         graph[b].append(a)  # 무방향 그래프

#     for i in range(1, V + 1):
#         if not visited[i]:  # 방문한 정점이 아니면, bfs 수행
#             result = bfs(i, 1)
#             if not result: break # False라면 바로 중단
#     print('YES' if result else 'NO')

# 복습용
import sys
from collections import deque
def bfs(start, group):
    visited[start] = group # 시작 정점 그룹 설정
    queue = deque([start])
    while queue: # queue가 비어있지 않을 동안
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i) # 하위 정점을 추가
                visited[i] = -1 * visited[x]
            elif visited[i] == visited[x]:
                return False
    return True


K = int(sys.stdin.readline())
for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (V+1)
    for i in range(1, V+1):
        if not visited[i]:
            answer = bfs(i, 1)
        if not answer: break
    print('YES' if answer else 'NO')