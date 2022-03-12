n = int(input())
num = list(map(int, input().split()))
cnt = 0

for i in num:
    tmp = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                tmp +=1
        if tmp == 0:
            cnt += 1

print(cnt)