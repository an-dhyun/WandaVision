import sys
N = int(sys.stdin.readline())
temp = N
for i in range(2, temp+1):
    while N%i==0:
        print(i)
        N = N//i