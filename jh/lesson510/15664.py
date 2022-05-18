n, m = map(int, input().split())
n_list = sorted(list(map(int, input().split())))
check = [False] * n
s= []

def dfs(start):
    if len(s) == m:
        print(*s)
        return
    temp = 0

    for i in range(start, len(n_list)):
        if not check[i] and temp != n_list[i]:
            check[i] = True
            s.append(n_list[i])
            temp = n_list[i]
            dfs(i+1)
            check[i] = False
            s.pop()

dfs(0)