N = int(input())
num = 666
cnt = 1
while cnt<N:
    num += 1
    answer = str(num).find('666')
    if answer != -1: cnt += 1
print(num)