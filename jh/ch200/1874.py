import sys
input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
stack = []
op = []
count = 1
tmp = True
for i in numbers:
    while count <= i:
        stack.append(count)
        op.append('+')
        count += 1
    if stack[-1] == i:
        stack.pop()
        op.append('-')
    else:
        tmp = False

if tmp:
    for i in op:
        print(i)
else:
    print("NO")