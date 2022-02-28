import sys
stack1 = list(sys.stdin.readline().strip())
stack2 = []

M = int(sys.stdin.readline())
for i in range(M):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'P':
        stack1.append(cmd[1])
    elif cmd[0]=='L': 
        if stack1:
            stack2.append(stack1.pop())
    elif cmd[0]=='D': 
        if stack2:
            stack1.append(stack2.pop())
    else:
        if stack1:
            stack1.pop()
stack1.append(reversed(stack2))
print(''.join(stack1))
        