n = int(input())
lst = [["*" for i in range(n)] for i in range(n)]

def star(x, y, n, lst):
    if n == 3:
        lst[x+1][y+1] = " "
    else:
        tmp = n // 3
        for i in range(x+tmp, x+2*tmp):
            for j in range(y+tmp, y+2*tmp):
                lst[i][j] = " "
        for i in range(0, n, tmp):
            for j in range(0, n, tmp):
                star(x+i, y+j, tmp, lst)

star(0, 0, n, lst)
for i in range(0, n):
    for j in range(0, n):
        print(lst[i][j], end="")
    print()