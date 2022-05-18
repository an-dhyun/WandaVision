n, m = map(int, input().split())
n_list = sorted(list(map(int, input().split())))
s= []

def dfs():
    if len(s) == m:
        print(*s)
        return
    temp = 0

    for i in range(0, len(n_list)):
        if temp != n_list[i]:
            s.append(n_list[i])
            temp = n_list[i]
            dfs()
            s.pop()

dfs()