n = int(input())
xy_list = []
rank = [1] * n
for i in range(n):
    xy = list(map(int, input().split()))
    xy_list.append(xy)
for i in range(n):
    for j in range(i+1, n):
        if (xy_list[i][0] < xy_list[j][0]) & (xy_list[i][1] < xy_list[j][1]):
            rank[i] += 1
        elif (xy_list[i][0] > xy_list[j][0]) & (xy_list[i][1] > xy_list[j][1]):
            rank[j] += 1
for i in rank:
    print(i, end=" ")