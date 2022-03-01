n = int(input())
lst = []
for i in range(n):
    lst = list(input())
    score = 0
    sum_score = 0
    for j in lst:
        if j == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)