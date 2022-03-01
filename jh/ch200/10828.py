import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    word = input().split()
    order = word[0]

    # push
    if order == "push":
        stack.append(word[1])
    
    # pop
    elif order == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    
    # size
    elif order == "size":
        print(len(stack))

    # empty
    elif order == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    # top
    elif order == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
