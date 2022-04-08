dp = [0, 1, 2, 4]
for i in range(4, 11):
    dp.append(dp[i-3]+dp[i-2]+dp[i-1])
for i in range(int(input())):
    n = int(input())
    print(dp[n])
# 1 = 1 :1
# 2 = 1+1 = 2 :2
# 3 = 1+1+1 = 2+1 = 1+2 = 3
# 4 = 1+1+1+1 = 1+1+2 = 1+2+1 = 2+1+1 = 2+2 = 1+3 = 3+1