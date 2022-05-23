from itertools import permutations
import sys

N = int(input())
A = list(map(int, input().split()))

per = permutations(A) # 리스트의 원소를 가지고 만들 수 있는 다양한 순열들을 반환
ans = 0

for i in per:
    s = 0
    for j in range(len(i)-1): s += abs(i[j] - i[j+1])
    if s > ans : ans = s

print(ans)