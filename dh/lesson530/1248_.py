# import sys
# n = int(sys.stdin.readline())
# tmp_s = list(sys.stdin.readline())
# S = []; idx = 0
# for i in range(n, 0, -1):
#     S.append([5]*(n-i)+tmp_s[idx:idx+i])
#     idx += i

# s = {}; visited = [False]*21
# def dfs(depth):
#     if depth == n:
#         print(*s[:n])
#         exit()
#     for i in range(-10, 11):
#         visited[i+10] = True
#         s[i] = i
#         check = True
#         for a in range(depth+1):
#             if (sum(s[a:depth+1])<0) and (S[a][depth] in {'0', '+'}): check=False
#             elif (sum(s[a:depth+1])>0) and (S[a][depth] in {'0', '-'}): check=False
#             elif (sum(s[a:depth+1])==0) and (S[a][depth] in {'-', '+'}): check=False
#         if check: # sign matrix 조건을 만족하면
#             dfs(depth + 1)
#             s.pop(i)
#             visited[i+10] = False
#         else: # 아니면
#             s.pop(i)
#             visited[i+10] = False
#             continue

# dfs(0)

def ck(idx):
    hap = 0
    for i in range(idx, -1, -1):
        hap += result[i]
        if hap == 0 and S[i][idx] != 0:
            return False
        elif hap < 0 and S[i][idx] >= 0:
            return False
        elif hap > 0 and S[i][idx] <= 0:
            return False
    return True

def solve(idx):
    if idx == N:
        return True
    if S[idx][idx] == 0:
        result[idx] = 0
        return solve(idx+1)
    for i in range(1, 11):
        result[idx] = S[idx][idx] * i
        if ck(idx) and solve(idx+1):
            return True
    return False

N = int(input())
arr = list(input())
S = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(i, N):
        temp = arr.pop(0)
        if temp == '+':
            S[i][j] = 1
        elif temp == '-':
            S[i][j] = -1

result = [0] * N
solve(0)
print(' '.join(map(str, result)))
 
