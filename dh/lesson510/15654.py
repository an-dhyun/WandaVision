def dfs():
    if len(s)==M:
        print(' '.join(map(str, s)))
    for i in range(N):
        if visited[i]: continue
        visited[i] = True
        s.append(nums[i])
        dfs()
        s.pop()
        visited[i] = False

N, M = map(int, input().split())
nums = list(map(int, input().split())) # 숫자 대신 배열
nums.sort()
s = []
visited = [False] * (N+1)

dfs()