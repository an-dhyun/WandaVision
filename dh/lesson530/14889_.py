import sys
N = int(sys.stdin.readline())
S = []
for _ in range(N):
    S.append(list(map(int, sys.stdin.readline().split())))

check = [False]*N
def dfs(depth, idx): # s 없애면 시간 줄어들음! ㅜㅜ
    global min_diff # dfs 함수 안에서 global로 설정해줘야 함
    if depth==N//2:
        start = 0; link = 0
        for i in range(N):
            for j in range(N):
                if check[i] and check[j]:  # start 능력치 계산
                    start += S[i][j]
                elif (not check[i]) and (not check[j]): # link 능력치 계산
                    link += S[i][j]
        min_diff = min(min_diff, abs(start-link))
        return
    for i in range(idx, N):
        if check[i] == False:
            check[i] = True
            dfs(depth+1, i)
            check[i] = False

min_diff = int(1e9)
dfs(0, 0)
print(min_diff)
