### 15655.py 참고

def dfs(start, depth):
    if depth == 6:
        print(*res)
        return

    for i in range(start, len(s)):
        res.append(s[i])
        dfs(i+1, depth+1)
        res.pop()

while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    del s[0]
    res = []
    dfs(0, 0)
    print()
