import sys
import operator 

# 값 받아오기
N = int(sys.stdin.readline())
words = []
for i in range(N):
    words.append(sys.stdin.readline().strip())

# 최대자릿수 계산
alph = {}
maxlen = 0
for i in words:
    if len(i) >= maxlen: maxlen = len(i)

# 자릿값 계산
for i in words:
    for j in range(len(i)):
        if i[j] not in alph:
            alph[i[j]] = 10**(len(i)-j-1) # 자릿수만큼 반환
        else:
            alph[i[j]] += 10**(len(i)-j-1)
alph = dict(sorted(alph.items(), key=lambda x: x[1], reverse=True))

# 합 계산
result = 0
num = 9
for i in alph:
    result += alph[i]*num
    num -= 1
print(result)