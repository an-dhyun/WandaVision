n, m = map(int, input().split())
n_list = sorted(list(map(int, input().split())))
s= []

def dfs(start):
    if len(s) == m:
        print(*s)
        return
    
    for i in range(start, n):
        if n_list[i] not in s:
            s.append(n_list[i])
            dfs(i+1)
            s.pop()

dfs(0)