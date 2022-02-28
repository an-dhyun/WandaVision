import sys
stack = []
def push(X):
    stack.append(X)
def top():
    if len(stack)==0: print(-1)
    else: print(stack[-1])
def size():
    print(len(stack))
def empty():
    if len(stack)==0: print(1)
    else: print(0)
def pop():
    if len(stack)==0: print(-1)
    else: 
        print(stack[-1])
        stack.pop(-1)
    
N = int(sys.stdin.readline())
for i in range(N):
    inp = list(sys.stdin.readline().split())
    if len(inp)==2:
        X = int(inp[1])
        push(X)
    else:
        if inp==['top']: top()
        elif inp==['size']: size()
        elif inp==['empty']: empty()
        elif inp==['pop']: pop()
        