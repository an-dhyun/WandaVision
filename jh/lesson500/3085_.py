import sys
input=sys.stdin.readline

def check():
    result = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            # 행
            if candy[j][i] == candy[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > result:
                result = cnt
        
        cnt = 1
        for j in range(1, n):
            # 열
            if candy[i][j] == candy[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > result:
                result = cnt
    return result

n = int(input())
candy = [list(input()) for _ in range(n)] # n*n array
m = 0

for i in range(n):
    for j in range(n):
        if i+1 < n:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            tmp = check()
            if tmp > m:
                m = tmp
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

        if j+1 < n:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            tmp = check()
            if tmp > m:
                m = tmp
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]

print(m)