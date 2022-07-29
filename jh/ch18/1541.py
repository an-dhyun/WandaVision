A = input().split('-')
B = []
for i in A:
    num = 0
    s = i.split('+')
    for j in s:
        num += int(j)
    B.append(num)
answer = B[0]
for i in range(1, len(B)):
    answer -= B[i]
    
print(answer)