n = int(input())
a = list(map(int, input().split()))
dpp = [0] * n
dpm = [0] * n
dp = [0] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dpp[i] < dpp[j]:
            dpp[i] = dpp[j]
    dpp[i] += 1

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if a[i] > a[j] and dpm[i] < dpm[j]:
            dpm[i] = dpm[j]
    dpm[i] += 1
for i in range(n):
    dp[i] = dpp[i] + dpm[i] - 1
print(max(dp))