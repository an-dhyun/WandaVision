import sys
S = list(sys.stdin.readline().strip().split('()'))
stack = 0
piece = 0
for i in S:
    here = list(i)
    stack += here.count("(")
    piece += stack
    stack -= here.count(")")
print(piece)