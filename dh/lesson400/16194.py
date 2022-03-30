N = int(input())
p = [0] + list(map(int, input().split())) # 각 장수별 가격
d = [0]*(N+1) # dp 행렬 - 각 장수별 최소 가격
d[1] = p[1] # 한장 구매하는 것은 가격이 정해져있음

for i in range(2, N+1):
    # 비교 : i-j장팩 + j장팩 vs i장 팩
    d[i] = d[i - 1] + p[1] 
    for j in range(2, i+1):
        if d[i] > d[i-j] + p[j]:
            d[i] = d[i-j] + p[j]

print(d[N])