nine = [int(input()) for i in range(9)]
m = sum(nine) - 100

for i in range(9):
    for j in range(i+1, 9):
        if m == nine[i] + nine[j]:
            n1, n2 = nine[i], nine[j] # 인덱스가 변하지 않게

# 인덱스가 변하지 않도록 for문 밖에 작성
nine.remove(n1)
nine.remove(n2)
nine.sort()

for i in nine:
    print(i)