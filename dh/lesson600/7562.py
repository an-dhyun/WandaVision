import sys
import collections
T = int(sys.stdin.readline())

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
for _ in range(T):
    l = int(sys.stdin.readline())
    now_x, now_y = map(int, sys.stdin.readline().rstrip().split())
    to_x, to_y = map(int, sys.stdin.readline().rstrip().split())

    queue = collections.deque()
    queue.append([now_x, now_y])

    visited = [[0]*l for _ in range(l)] # 방문 처리 빼먹지 말기
    visited[now_x][now_y] = 1

    while queue:
        x, y = queue.popleft()
        if x==to_x and y==to_y: 
            print(visited[x][y]-1)
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<=nx<l) and (0<=ny<l) and (visited[nx][ny]==0):
                print(nx, ny)
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
