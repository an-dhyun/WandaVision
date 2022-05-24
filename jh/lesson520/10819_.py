### 백트래킹

n = int(input())
arr = list(map(int, input().split()))
temp = []
res = []

def dfs(x):
    if x == n:
        res.append(sum(abs(arr[temp[i]]-arr[temp[i+1]]) for i in range(n-1)))
        return
    for i in range(n):
        if i not in temp:
            temp.append(i)
            dfs(x+1)
            temp.pop()

dfs(0)
print(max(res))