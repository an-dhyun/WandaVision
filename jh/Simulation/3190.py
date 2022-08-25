# 백준 - 뱀
from collections import deque

N = int(input())
K = int(input())
apple = [[0]*N for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    apple[r-1][c-1] = 1
snake = deque([[0, 0]])
count = 0

nx, ny = 0, 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
d = 1 # 동
direction = {}

L = int(input())
for _ in range(L):
    X, C = input().split()
    direction[int(X)] = C

def turn_direction(C):
    global d
    if C == 'D':
        d = (d+1)%4
    else:
        d = (d-1)%4

while True:
    count += 1
    nx += dx[d]
    ny += dy[d]

    if count in direction.keys():
        turn_direction(direction[count])

    if nx>=0 and nx<N and ny>=0 and ny<N:
        if [nx, ny] in snake:
            break
        # 사과가 있는 경우
        if apple[nx][ny] == 1:
            apple[nx][ny] = 0
            snake.append([nx, ny])
        # 사과가 없는 경우
        else:
            snake.append([nx,ny])
            snake.popleft()
    else:
        break

print(count)
