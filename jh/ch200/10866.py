import sys
input = sys.stdin.readline

N = int(input())
deq = []

for _ in range(N):
    com = input().split()

    # push_front
    if com[0] == "push_front":
        deq.insert(0, int(com[1]))
    
    # push_back
    elif com[0] == "push_back":
        deq.append(int(com[1]))
    
    # pop_front
    elif com[0] == "pop_front":
        if deq != []:
            print(deq.pop(0))
        else:
            print(-1)
    
    # pop_back
    elif com[0] == "pop_back":
        if deq != []:
            print(deq.pop(-1))
        else:
            print(-1)
    
    # size
    elif com[0] == "size":
        print(len(deq))

    # empty
    elif com[0] == "empty":
        if deq == []:
            print(1)
        else:
            print(0)
    
    # front
    elif com[0] == "front":
        if deq != []:
            print(deq[0])
        else:
            print(-1)

    # back
    elif com[0] == "back":
        if deq != []:
            print(deq[-1])
        else:
            print(-1)