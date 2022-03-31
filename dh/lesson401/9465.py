import sys
T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    dp = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(2)]

    # 두번째 줄은 무조건 첫번째 줄 대각선방향을 뗀거랑 합해야함
    dp[0][1] = dp[1][0] + dp[0][1]
    dp[1][1] = dp[0][0] + dp[1][1]
    
    # 세번째줄부터는 대각선방향의 연속 두개를 고려해야함
    for j in range(2, n):
        dp[0][j] = max(dp[1][j-1], dp[1][j-2]) + dp[0][j]
        dp[1][j] = max(dp[0][j-1], dp[0][j-2]) + dp[1][j]

    print(max(dp[0][n-1], dp[1][n-1]))