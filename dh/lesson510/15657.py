def dfs(n):
    if len(s)==M:
        print(' '.join(map(str, s)))
        return
    for i in range(n, N):
        visited[i] = True
        s.append(nums[i])
        dfs(i)
        s.pop()
        visited[i] = False

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
s = []
visited = [False] * (N+1)

dfs(0)