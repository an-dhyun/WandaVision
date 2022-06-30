# import sys
# N, S = map(int, sys.stdin.readline().split())
# nums = list(map(int, sys.stdin.readline().split()))

# s = []; check = [False]*N
# def dfs(n):
#     global cnt
#     global pass_cmd
#     if (sum(s)==S) and (len(s)>=1):
#         print(s)
#         cnt += 1
#         if n==N-1: 
            
#         else: pass_cmd = False
#         return
#     for i in range(n, N):
#         if check[i] == False:
#             check[i] = True
#             s.append(nums[i])
#             dfs(i)
#             if pass_cmd: 
#                 s = []
#                 pass
#             else:
#                 s.pop()
#                 check[i] = False

# cnt = 0; pass_cmd = False
# dfs(0)
# print(cnt)

import sys
from itertools import combinations

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, n+1):
    comb = combinations(arr, i)

    for x in comb:
        if sum(x) == s:
            cnt += 1

print(cnt)