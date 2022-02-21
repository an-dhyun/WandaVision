N = int(input())
num = 2
while N>1:
    while N%num == 0:
        print(num)
        N = N//num
    num += 1