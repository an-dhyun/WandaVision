# 종이 한간당 가로, 세로 2가지 경우가 가능함
# 참고 : https://lagooni.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%A2%85%EC%9D%B4-%EC%A1%B0%EA%B0%81-14391%EB%B2%88-Python-Bitmasking

def bitmask():
    global maxAns
    for i in range(1 << n * m): # 비트마스크로 2^(N*M)(=1<<n*m)의 경우의 수를 따져본다
        total = 0 # total : 해당 경우의 합을 저장할 변수
        for row in range(n): # 가로 합(rowsum) 계산
            rowsum = 0
            for col in range(m):
                idx = row * m + col # idx : 이차원 배열을 일렬로 늘렸을때의 해당 값의 인덱스가 어디인지 
                if i & (1 << idx) != 0: # idx번째 칸의 종이가 가로방향(1)일 때
                    rowsum = rowsum * 10 + arr[row][col] # 한 row를 돌면서 연속으로 가로방향이 나온다면 자릿수를 그에 맞춰줘야 함(10을 곱함)
                else: # 세로방향(0)일 때 
                    total += rowsum # 가로방향 종이가 끊어졌다는 뜻이므로, 앞에서 나온 수를 total에 더하고
                    rowsum = 0 # rowsum 초기화
            total += rowsum

        for col in range(m): # 세로 합(colsum) 계산
            colsum = 0
            for row in range(n):
                idx = row * m + col
                if i & (1 << idx) == 0: # 세로일때
                    colsum = colsum * 10 + arr[row][col]
                else: # 가로일때 
                    total += colsum
                    colsum = 0
            total += colsum
        maxAns = max(maxAns, total)


n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

maxAns = 0
bitmask()
print(maxAns)
