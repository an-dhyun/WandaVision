n = int(input())
for i in range(n):
    lst = list(map(int, input().split()))
    cnt = 0
    for j in range(lst[0]):
        mean = sum(lst[1:]) / lst[0]
        if lst[j+1] > mean:
            cnt += 1
    print("{:.3f}%".format(cnt/lst[0]*100))