n, m = map(int, input().split())
chess = []
mini = []
for i in range(n):
    chess.append(input())
for a in range(n - 7):
    for b in range(m - 7):
        idx1 = 0 # start with W
        idx2 = 0 # start with B
        for i in range(a, a+8):
            for j in range(b, b+8): # 8*8 chess
                if (i + j) % 2 == 0:
                    if chess[i][j] != 'W':
                        idx1 += 1
                    elif chess[i][j] != 'B':
                        idx2 += 1
                else:
                    if chess[i][j] != 'B':
                        idx1 += 1
                    elif chess[i][j] != 'W':
                        idx2 += 1
        mini.append(idx1) # start with W
        mini.append(idx2) # start with B
print(min(mini))