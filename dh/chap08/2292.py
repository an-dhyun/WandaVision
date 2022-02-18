N = int(input())-1
cnt = 1
while True:
    if N<=0: 
        print(cnt)
        break
    else:
        N -= cnt*6
        cnt += 1