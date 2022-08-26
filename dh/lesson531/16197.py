import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
board = []
x, y = [], []
for _ in range(N):
    board.append(list(sys.stdin.readline()))

for row in range(N): # 동전 위치 찾기
    for col in range(M):
        if board[row][col]=='o': 
            x.append(row)
            y.append(col)

dx = [0, 0, 1, -1] # 세로방향 이동
dy = [-1, 1, 0, 0] # 가로방향 이동

def chk_in(lst): # 떨어졌는지 확인
    if 0<=lst[0]<N and 0<=lst[1]<M: return 1
    else: return -1
def chk_wall(lst): # 벽인지 확인
    if board[lst[0]][lst[1]]=='#': return 1
    else: return -1

def dfs(cnt):
    global x, y
    print(cnt, x, y)
    if cnt>=10:
        print(-1)
        exit() # 10회 넘어가면 stop
    
    cnt += 1
    for i in range(4):
        new_c1 = [x[0]+dx[i], y[0]+dy[i]]
        new_c2 = [x[1]+dx[i], y[1]+dy[i]]
        if chk_wall(new_c1)==-1: # 벽인지 확인하고 이동
            x[0] = new_c1[0]; y[0] = new_c1[1]
        if chk_wall(new_c2)==-1:
            x[1] = new_c2[0]; y[1] = new_c2[1]

        print(x, y)
        if chk_in([x[0], y[0]]) * chk_in([x[1], y[1]]) < 0: # 하나만 떨어졌다면 stop
            print(cnt)
            exit()
        else: 
            dfs(cnt)

dfs(0)