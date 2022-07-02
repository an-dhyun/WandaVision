def bitmask():
    global maxAns

    for i in range(1 << n*m): # 2^(n*m) 경우의 수
        total = 0
        for row in range(n):
            rowsum = 0 # 가로합
            for col in range(m):
                idx = row * m + col
                if i & (1 << idx) != 0: # 가로
                    rowsum = rowsum*10 + arr[row][col]
                else:
                    total += rowsum
                    rowsum = 0
            total += rowsum
        
        for col in range(m):
            colsum = 0 # 세로합
            for row in range(n):
                idx = row * m + col
                if i & (1 << idx) == 0: # 세로
                    colsum = colsum*10 + arr[row][col]
                else:
                    total += colsum
                    colsum = 0
            total += colsum
        
        maxAns = max(maxAns, total)

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

maxAns = 0
bitmask()
print(maxAns)