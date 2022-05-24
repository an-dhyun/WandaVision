import sys
n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
res = sys.maxsize

# 시작 도시, 다음 도시, 비용, 방문 여부
def dfs(start, next, value, visit):
    global res

    if len(visit) == n:
        if w[next][start] != 0: # 비용이 0이 아니면
            res = min(res, value + w[next][start]) # 최솟값과 비교해서 대입
        return
    
    for i in range(n):
        if w[next][i] != 0 and i not in visit and value < res:
            visit.append(i)
            dfs(start, i, value + w[next][i], visit)
            visit.pop()

# 도시 마다 출발점 지정
for i in range(n):
    dfs(i, i, 0, [i])

print(res)