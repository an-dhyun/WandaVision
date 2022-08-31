# import sys

# N, M = map(int, sys.stdin.readline().rstrip().split())
# board = []
# x, y = [], []
# for _ in range(N):
#     board.append(list(sys.stdin.readline()))

# for row in range(N): # 동전 위치 찾기
#     for col in range(M):
#         if board[row][col]=='o': 
#             x.append(row)
#             y.append(col)

# dx = [0, 0, 1, -1] # 세로방향 이동
# dy = [-1, 1, 0, 0] # 가로방향 이동

# def chk_in(lst): # 떨어졌는지 확인
#     if 0<=lst[0]<N and 0<=lst[1]<M: return 1
#     else: return -1
# def chk_wall(lst): # 벽인지 확인
#     if board[lst[0]][lst[1]]=='#': return 1
#     else: return -1

# def dfs(cnt):
#     global x, y
#     print(cnt, x, y)
#     if cnt>=10:
#         print(-1)
#         exit() # 10회 넘어가면 stop
    
#     cnt += 1
#     for i in range(4):
#         new_c1 = [x[0]+dx[i], y[0]+dy[i]]
#         new_c2 = [x[1]+dx[i], y[1]+dy[i]]
#         if chk_wall(new_c1)==-1: # 벽인지 확인하고 이동
#             x[0] = new_c1[0]; y[0] = new_c1[1]
#         if chk_wall(new_c2)==-1:
#             x[1] = new_c2[0]; y[1] = new_c2[1]

#         print(x, y)
#         if chk_in([x[0], y[0]]) * chk_in([x[1], y[1]]) < 0: # 하나만 떨어졌다면 stop
#             print(cnt)
#             exit()
#         else: 
#             dfs(cnt)

# dfs(0)

from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    while coin:
        x1, y1, x2, y2, cnt = coin.popleft()

        if cnt >= 10: # 횟수가 10회 넘어가면 -1 리턴
            return -1

        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]

            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
                # 벽이라면
                if board[nx1][ny1] == "#": # 되돌려놓음
                    nx1, ny1 = x1, y1
                if board[nx2][ny2] == "#":
                    nx2, ny2 = x2, y2
                coin.append((nx1, ny1, nx2, ny2, cnt + 1))
            elif 0 <= nx1 < n and 0 <= ny1 < m:  # coin2가 떨어진 경우
                return cnt + 1 # 횟수 리턴
            elif 0 <= nx2 < n and 0 <= ny2 < m:  # coin1가 떨어진 경우
                return cnt + 1 # 횟수 리턴
            else:  # 둘 다 빠진 경우 무시
                continue

    return -1

n, m = map(int, input().split())

coin = deque()
board = [] # 보드 상태 기록
temp = [] # 동전의 위치 기록
for i in range(n):
    board.append(list(input().strip()))
    for j in range(m):
        if board[i][j] == "o":
            temp.append((i, j)) # 동전이 있다면 기록

coin.append((temp[0][0], temp[0][1], temp[1][0], temp[1][1], 0)) # 두 좌표, 버튼을 누른 횟수 기록

print(bfs())