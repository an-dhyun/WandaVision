def dfs():
    if len(s)==M: 
        print(*s)
        return
    remember_me = 0
    for i in range(N):
        if (visited[i]) or (remember_me == nums[i]): continue
        visited[i] = True
        remember_me = nums[i]
        s.append(nums[i])
        dfs()
        s.pop()
        visited[i] = False

answer = []

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
s = []
visited = [False] * (N+1)

dfs()