import sys
input = sys.stdin.readline

T = int(input())
vps = [list(input().rstrip()) for _ in range(T)]

for i in range(T):
    stack = []
    for j in vps[i]:
        if j == "(":
            stack.append(j)
        elif j == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
                break # no vps
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")