dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def bfs(i, j):
    s[i][j] = 0
    que = [[i, j]]
    while que:
        a, b = que[0][0], que[0][1]
        del que[0]
        for k in range(8):
            x = a+dx[k]
            y = b+dy[k]
            if 0 <= x < h and 0 <= y < w and s[x][y] == 1:
                s[x][y] = 0
                que.append([x, y])

while(1):
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    s = []
    cnt = 0
    for i in range(h):
        s.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if s[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)