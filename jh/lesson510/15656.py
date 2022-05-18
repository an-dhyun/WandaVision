n, m = map(int, input().split())
n_list = sorted(list(map(int, input().split())))
s= []

def dfs():
    if len(s) == m:
        print(*s)
        return
    
    for i in range(0, n):
        s.append(n_list[i])
        dfs()
        s.pop()

dfs()