T = int(input())
for i in range(T):
    k = int(input()); n = int(input())
    list = [x for x in range(1, n+1)]
    for i in range(k):
        new_list = [0]*n
        for i in range(n):
            new_list[i] = sum(list[:i+1])
        list = new_list
    print(list)