import sys

def check(colors):
    N = len(colors)
    answer = 1 # 행, 열 기준 가장 긴 길이 

    for i in range(N): 
        cnt = 1
        for j in range(1, N): # 열방향 카운트
            if colors[i][j] == colors[i-1][j]: cnt += 1
            else: cnt = 1
        if cnt > answer: answer = cnt

        cnt = 1
        for j in range(1, N): # 행방향
            if colors[i][j] == colors[i][j-1]: cnt += 1
            else: cnt = 1
        if cnt > answer: answer = cnt

    return answer

N = int(sys.stdin.readline())
colors = [list(sys.stdin.readline()) for _ in range(N)]
maxanswer = 0

for i in range(N): # 행방향 바꾸기
    for j in range(N):
        if j+1 < N:
            colors[i][j], colors[i][j+1] = colors[i][j+1], colors[i][j]
            cnt = check(colors)
            if cnt > maxanswer: maxanswer = cnt
            colors[i][j], colors[i][j+1] = colors[i][j+1], colors[i][j]
        
        if i+1 < N:
            colors[i][j], colors[i+1][j] = colors[i+1][j], colors[i][j]
            cnt = check(colors)
            if cnt > maxanswer: maxanswer = cnt
            colors[i][j], colors[i+1][j] = colors[i+1][j], colors[i][j]

print(maxanswer)

