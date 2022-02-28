import sys
d = []
def push_front(X): d.insert(0, X)
def push_back(X): d.append(X)
def pop_front(): 
    if len(d)==0: print(-1)
    else: 
        print(d[0])
        d.pop(0)
def pop_back(): 
    if len(d)==0: print(-1)
    else:
        print(d[-1]) 
        d.pop(-1)
def size(): print(len(d))
def empty():
    if len(d)==0: print(1)
    else: print(0)
def front():
    if len(d)==0: print(-1)
    else: print(d[0])
def back():
    if len(d)==0: print(-1)
    else: print(d[-1])
    
for _ in range(int(sys.stdin.readline())):
    cmd = list(sys.stdin.readline().split())
    if cmd[0]=='push_front': push_front(int(cmd[1]))
    elif cmd[0]=='push_back': push_back(int(cmd[1]))
    elif cmd[0]=='pop_front': pop_front()
    elif cmd[0]=='pop_back': pop_back()
    elif cmd[0]=='size': size()
    elif cmd[0]=='empty': empty()
    elif cmd[0]=='front': front()
    else: back()
    