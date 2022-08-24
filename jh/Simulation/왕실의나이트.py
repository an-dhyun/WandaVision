data = input()
row = int(data[-1])
col = ord(data[0]) - ord('a') + 1

moves = [(-2,-1), (-2,1), (-1,-2), (-1,2),
         (1,-2), (1,2), (2,-1), (2,1)]

answer = 0
for move in moves:
    nrow = row + move[0]
    ncol = col + move[1]
    if nrow >= 1 and ncol >=1 and nrow <=8 and ncol <=8:
        answer += 1

print(answer)