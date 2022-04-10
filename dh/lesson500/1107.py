import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
broken = []
if M!=0:
    broken = list(map(int, sys.stdin.readline().split()))

answer = abs(N-100) # 100에서 직접 이동하는 경우
if N==100: print(0)
else:
    for i in range(1000001):
        check = True
        for j in list(str(i)):
            if int(j) in broken: 
                check = False # 금지된 숫자가 있을경우 pass하도록!
        if (check == True) & (abs(N-i)+len(str(i)) < answer):
            answer = abs(N-i)+len(str(i)) # 기준숫자 길이 + 이동 횟수
    print(answer)


