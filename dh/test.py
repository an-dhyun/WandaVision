def hansu(n):
    cnt = 0
    for i in range(1, n+1):
        lst = list(map(int, str(i)))
        print(lst)
        if i < 100:
            cnt += 1
        elif (lst[2] - lst[1]) == (lst[1] - lst[0]):
            print("yes")
            cnt += 1
    return cnt

n = int(input())
print(hansu(n))