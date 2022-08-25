import sys
sys.setrecursionlimit(1000)

N, M = map(int, sys.stdin.readline().split())
nums = []
for i in range(N):
    nums.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [1, -1, 0, 0] # 세로축방향 이동
dy = [0, 0, 1, -1] # 가로축방향 이동

maxAnswer = -1e9
visited = [[False]*M for _ in range(N)]
max_val = max(map(max, nums))
def dfs(x, y, result, chk):
    global maxAnswer, visited
    if maxAnswer >= result + max_val * (3-chk):
        return
    if chk==3:
        maxAnswer = max(maxAnswer, result) # 4회차일 경우 값 비교
        return
    for i in range(0, 4):
        nx = x+dx[i] # 다음칸 세로위치
        ny = y+dy[i] # 다음칸 가로위치
        if (0<=nx<N and 0<=ny<M) and (visited[nx][ny]==False): # 범위 내에 있을 경우
            if chk==1: # 두번째이면
                visited[nx][ny]=True # 방문표시
                dfs(x, y, result+nums[nx][ny], chk+1) # 위치만 고정하고 더해줌 -> ㅗ자모양 해결
                visited[nx][ny]=False # 돌아옴
            visited[nx][ny]=True # 방문표시
            dfs(nx, ny, result+nums[nx][ny], chk+1) # 다음이동
            visited[nx][ny]=False # 돌아옴

for i in range(N):
    for j in range(M):
        visited[i][j]=True
        dfs(i, j, nums[i][j], 0) # 1회차 시작하고 넣음
        visited[i][j]=False
print(maxAnswer)