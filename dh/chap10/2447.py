import math
N = int(input())
star = ['*']*N
stars = []
for i in range(N):
    stars.append(star.copy())

def count(N):
    result = 0
    while True:
        if N//3>=1: 
            result += 1
            N = N//3
        else:
            break
    return result

def remove(N_tmp): # 크기에 따라 별을 지우는 함수
    num = count(N_tmp) # 승수 계산
    if num>=1: 
        iter = int(3**(num-1)) # 지울 간격 계산
        row = iter; col = iter # 지우기 시작할 좌표 계산
        while True:
            for i in range(row, row+iter):
                for j in range(col, col+iter):
                    stars[i][j] = ' '
            if col + iter*3 >= N and row + iter*3 >= N: 
                break # 행, 열 모두 끝까지 도달한 경우 while문 종료
            elif col + iter*3 >= N:
                row += iter*3
                col = iter # 열만 끝까지 도달한 경우 다음 행으로 이동
            else:
                col += iter*3 # 둘다 아닐 경우 다음 열로 이동
        N_tmp = N_tmp//3 # 한번 지우고나서 크기값을 3으로 나눠줌
        remove(N_tmp) # 재귀호출

remove(N)

for i in stars:
    for j in i:
        print(j, end='')
    print()