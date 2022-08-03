for _ in range(int(input())):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    cnt = 1
    
    A.sort(key=lambda x: x[0])
    m = A[0][1]
    for i in range(1, N):
        if m > A[i][1]:
            cnt += 1
            m = A[i][1]
    
    print(cnt)