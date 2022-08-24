N, M = map(int, input().split())
x, y, direction = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]
d = [[0]*M for _ in range(N)]
d[x][y] = 1

# 북, 동, 남, 서
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        x = nx
        y = ny
        count += 1
        turn_time = 0
        d[x][y] = 1
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
            turn_time = 0
        else:
            break

print(count)