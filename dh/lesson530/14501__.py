# import sys
# N = int(sys.stdin.readline())
# Ts = []; Ps = []; check = [False]*N

# for _ in range(N):
#     T, P = map(int, sys.stdin.readline().split())
#     Ts.append(T); Ps.append(P)

# s = []; results = []
# def cal(i):
#     if (i+Ts[i]==N-1) and (Ts[i+Ts[i]]==1): 
#         s.append(Ps[i+Ts[i]])
#     elif i+Ts[i] > N-1: 
#         print(s)
#         results.append(sum(s))
#         return 
#     check[i] = True
#     s.append(Ps[i])
#     cal(i+Ts[i])
#     s.pop()
#     check[i] = False

# for i in range(N): cal(i)
# print(max(results))

n = int(input())
t = []
p = []
dp = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)
for i in range(n - 1, -1, -1): # 거꾸로 푸는것의 차이 ..
    if t[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
print(dp[0])