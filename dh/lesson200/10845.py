import sys
q = []
def push(X): q.append(X)
def pop(): 
    if len(q)==0: print(-1)
    else: 
        print(q[0])
        q.pop(0)
def size():
    print(len(q))
def empty():
    if len(q)==0: print(1)
    else: print(0)
def front():
    if len(q)==0: print(-1)
    else: print(q[0])
def back():
    if len(q)==0: print(-1)
    else: print(q[-1])

N = int(sys.stdin.readline())
for _ in range(N):
    cmd = list(sys.stdin.readline().split())
    if cmd[0]=='push':
        push(int(cmd[1]))
    elif cmd[0]=='pop': pop()
    elif cmd[0]=='size': size()
    elif cmd[0]=='empty': empty()
    elif cmd[0]=='front': front()
    else: back()
    
    