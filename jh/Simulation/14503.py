# 백준 - 로봇청소기

N, M = map(int, input().split())
r, c, d = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]

move = [[0]*M for _ in range(N)]
move[r][c] = 1

dr=[-1,0,1,0]
dc=[0,1,0,-1]

def turn_left():
    global d
    d -= 1
    if d==-1:
        d=3

turn = 0
count = 1

while True:
    turn_left()
    nr = r+dr[d]
    nc = c+dc[d]

    if array[nr][nc] == 0 and move[nr][nc] == 0:
        r, c = nr, nc
        count += 1
        turn = 0
        move[r][c] = 1
        continue
    else:
        turn += 1

    if turn == 4:
        nr = r-dr[d]
        nc = c-dc[d]
        if array[nr][nc] == 0:
            r, c = nr, nc
        else:
            break
        turn = 0

print(count)
