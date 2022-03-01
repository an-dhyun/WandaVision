import sys
input = sys.stdin.readline

N = int(input())
que = []

for _ in range(N):
    com = input().split()

    # push
    if com[0] == "push":
        que.insert(0, int(com[1]))
    
    # pop
    if com[0] == "pop":
        if que != []:
            print(que.pop())
        else:
            print(-1)
    
    # size
    if com[0] == "size":
        print(len(que))
    
    # empty
    if com[0] == "empty":
        if que == []:
            print(1)
        else:
            print(0)

    # front
    if com[0] == "front":
        if que != []:
            print(que[-1])
        else:
            print(-1)
    
    # back
    if com[0] == "back":
        if que != []:
            print(que[0])
        else:
            print(-1)