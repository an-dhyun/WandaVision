N, M = map(int, input().split())
first_chess = []
second_chess = []
for i in range(8):
    line_f = []
    line_s = []
    for j in range(8):
        if j%2==0: 
            line_f.append('W')
            line_s.append('B')
        else:
            line_f.append('B')
            line_s.append('W')
    if i%2==0:
        first_chess.append(line_f)
        second_chess.append(line_s)
    else:
        first_chess.append(line_s)
        second_chess.append(line_f)

input_chess = []
for i in range(N):
    input_line = input()
    to_list = list(map(str, input_line))
    input_chess.append(to_list)

# 첫번째 체스판과의 비교
first_cnt = []
for i in range(0, N-7):
    for j in range(0, M-7):
        cnt = 0
        for a in range(8):
            for b in range(8):
                if input_chess[i+a][j+b] != first_chess[a][b]: cnt += 1
        first_cnt.append(cnt)
        
first_min = min(first_cnt)

# 두번쨰 체스판과의 비교
second_cnt = []
for i in range(0, N-7):
    for j in range(0, M-7):
        cnt = 0
        for a in range(8):
            for b in range(8):
                if input_chess[i+a][j+b] != second_chess[a][b]: cnt += 1
        second_cnt.append(cnt)
second_min = min(second_cnt)

print(min(first_min, second_min))