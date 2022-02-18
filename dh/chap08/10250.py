T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    floor = N%H
    hori = N//H + 1
    if floor==0: 
        floor = H
        hori -= 1
    num = '%s%02d'%(floor, hori)
    print(num)