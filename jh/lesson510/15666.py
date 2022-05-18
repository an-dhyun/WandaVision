n, m = map(int, input().split())
n_list = sorted(list(map(int, input().split())))
s= []

def dfs(start):
    if len(s) == m:
        print(*s)
        return
    temp = 0

    for i in range(start, len(n_list)):
        if temp != n_list[i]:
            s.append(n_list[i])
            temp = n_list[i]
            dfs(i)
            s.pop()

dfs(0)