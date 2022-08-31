from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
board = []
temp = []
coin = deque()

for i in range(N):
    board.append(list(sys.stdin.readline()))
    for j in range(M):
        if board[i][j]=='o': temp.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while coin:
        x1, y1, x2, y2, cnt = coin.popleft()
        if cnt >= 10:
            return -1

        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]

            if 0<=nx1<N and 0<=ny1<M and 0<=nx2<N and 0<=ny2<M:
                if board[nx1][ny1]=='#':
                    nx1 = x1
                    ny1 = y1
                elif board[nx2][ny2]=='#':
                    nx2 = x2
                    ny2 = y2
                coin.append((nx1, ny1, nx2, ny2, cnt+1))
            elif 0<=nx1<N and 0<=ny1<M:
                return cnt+1
            elif 0<=nx2<N and 0<=ny2<M:
                return cnt+1
            else: 
                continue
    return -1


coin.append((temp[0][0], temp[0][1], temp[1][0], temp[1][1], 0))
print(bfs())