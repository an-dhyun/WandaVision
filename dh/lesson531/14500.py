import sys

N, M = map(int, sys.stdin.readline().split())
nums = []
for i in range(N):
    nums.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [1, -1, 0, 0] # 세로축방향 이동
dy = [0, 0, 1, -1] # 가로축방향 이동

maxAnswer = -1e9
visited = [[False]*M for _ in range(N)]
s = []
def dfs(plc, chk):
    global maxAnswer, visited
    if chk==4:
        if maxAnswer < sum(s): maxAnswer = sum(s)
        return
    for i in range(0, 4):
        nx = plc[0]+dx[i]
        ny = plc[1]+dy[i]
        if (0<=nx<N and 0<=ny<M):
            if visited[nx][ny]==False: 
                visited[nx][ny]=True
                s.append(nums[nx][ny])
                dfs([nx, ny], chk+1)
                visited[nx][ny]=False
                s.pop()
            else:
                dfs([nx, ny], chk)

for i in range(N):
    for j in range(M):
        dfs([i, j], 0)
print(maxAnswer)