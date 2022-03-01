import sys
input = sys.stdin.readline

T = int(input())
stack = [list(input().split()) for _ in range(T)]

for i in range(T):
    for j in stack[i]:
        print("".join(reversed(list(j))), end=" ")
    print()