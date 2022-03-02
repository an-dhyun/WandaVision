import sys
input = sys.stdin.readline

S = list(input().rstrip()) # one by one
stack = []
result = 0

for i in range(len(S)):
    # (
    if S[i] == '(':
        stack.append('(')
    
    # )
    else:
        # laser: ()
        if S[i-1] == '(':
            stack.pop()
            result += len(stack)
        
        # end of bar: ))
        else:
            stack.pop()
            result += 1

print(result)
