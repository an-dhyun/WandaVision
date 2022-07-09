import sys
import collections 

'''
📍 DFS가 적합한 유형
- 검색 대상 그래프가 큰 경우(정점과 간선의 개수가 많음)
- 경로의 특징을 저장해둬야 하는 문제
ex) 각 정점에 숫자가 적혀있고 a부터 b까지 가는 경로를 구하는 데 경로에 같은 숫자가 있으면 안된다는 문제
BFS는 경로의 특징을 가지지 못함

📍 BFS가 적합한 유형
- 미로찾기 등 최단거리를 구해야 할 경우
- DFS는 처음으로 발견되는 해답이 최단거리 라는 것 보장 X
- 반면 BFS는 현재 노드에서 가까운 곳부터 찾기 때문에 경로 탐색 시 첫번째로 찾아지는 해답이 곧 최단거리이다.
'''

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    lst = list(map(int, list(sys.stdin.readline().rstrip())))
    graph.append(lst)

queue = collections.deque([(0,0)])
result = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < M) and (graph[nx][ny]==1):
           graph[nx][ny] = graph[x][y]+1
           queue.append((nx, ny))

print(graph[N-1][M-1])