while True:
    def dfs(n):
        if len(s)==6:
            print(*s)
        for i in range(n, k):
            if visited[i]: continue
            visited[i] = True
            s.append(nums[i])
            dfs(i)
            s.pop()
            visited[i] = False

    nums = list(map(int, input().split()))
    if nums==[0]: break

    k = nums[0]
    nums = nums[1:]

    s = []
    visited = [False]*(k+1)

    dfs(0)
    print()