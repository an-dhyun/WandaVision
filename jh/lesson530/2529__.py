k = int(input())
op = input().split()
visit = [False] * 10
m, n = "", ""

def possible(i, j, k):
    if k == ">":
        return i>j
    else:
        return i<j

def solve(cnt, s):
    global m, n
    if cnt == k + 1: # 재귀 함수 종료 조건
        if len(n) == 0:
            n = s
        else:
            m = s
        return
    for i in range(10):
        if not visit[i]: # 수를 중복하여 사용할 수 없음
            if cnt == 0 or possible(s[-1], str(i), op[cnt-1]):
                visit[i] = True
                solve(cnt+1, s+str(i))
                visit[i] = False

solve(0, "")
print(m)
print(n)