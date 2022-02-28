import sys
T = int(sys.stdin.readline())
for i in range(T):
    sentence = list(sys.stdin.readline().split())
    for i in sentence:
        temp = list(i)
        temp.reverse()
        for j in temp: print(j, end='')
        print(' ', end='')
    print()