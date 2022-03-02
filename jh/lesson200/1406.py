import sys
input = sys.stdin.readline

word = list(input().strip())
stack = []
M = int(input())

for _ in range(M):
    com = input().split()
    
    if com[0] == "L" and len(word) != 0:
        stack.append(word.pop())

    elif com[0] == "D" and len(stack) != 0:
        word.append(stack.pop())

    elif com[0] == "B" and len(word) != 0:
        word.pop()
    
    elif com[0] == "P":
        word.append(com[1])

print("".join(word + list(reversed(stack))))