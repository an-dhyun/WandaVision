import sys
n = int(sys.stdin.readline())
answer = [] # 정답 리스트
list = [] # 준비 리스트
mark = [] # 기호 리스트
for i in range(n):
    answer.append(int(sys.stdin.readline()))
idx = 0
for i in range(1, n+1):
    list.append(i)
    mark.append("+")
    while True:
        if len(list) != 0 and list[-1] == answer[idx]: # 넣은 원소가 필요한 경우
            list.pop(-1)
            mark.append("-")
            idx += 1
        else: break
if len(list)==0: 
    for i in mark: print(i)
else:
    print("NO")