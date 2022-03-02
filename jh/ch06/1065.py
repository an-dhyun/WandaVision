def hansu():
    x = int(input())
    cnt = 0
    for i in range(1, x+1):
        lst = list(map(int, str(i)))
        if i < 100:
            cnt += 1
        elif lst[2]-lst[1] == lst[1]-lst[0]:
            cnt += 1
    print(cnt)
hansu()
