n = int(input())
N = 1
cnt = 1
while n > N:
    N += 6 * cnt
    cnt += 1
print(cnt)