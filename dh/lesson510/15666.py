def dfs(n):
    if len(s)==M: 
        print(*s)
        return
    remember_me = 0
    for i in range(n, N):
        if remember_me != nums[i]:
            visited[i] = True
            s.append(nums[i])
            remember_me = nums[i]
            dfs(i)
            s.pop()
            visited[i] = False

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
s = []
visited = [False] * (N+1)

dfs(0)