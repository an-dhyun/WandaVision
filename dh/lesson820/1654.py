import sys
N, K = map(int, sys.stdin.readline())
haves = []
for _ in range(N):
    haves.append(sys.stdin.readline())

start, end = 1, max(haves) # 이분 탐색의 처음(가장 짧은 길이), 끝(가장 긴 길이)

while start <= end: # 가장 짧은 길이에서 긴 길이까지 돌때까지 반복
    mid = (start + end) // 2 # 이분 탐색의 중간(start, end)의 중간
    lines = 0 # 랜선 개수
    for i in haves:
        lines += i // mid # 분할된 랜선 개수

    if lines >= N: # 랜선의 개수가 분기점 - 목표치 이상일 경우
        start = mid + 1 # 길이를 더 늘림
    else: # 목표치 이하일 경우 
        end = mid - 1 # 길이를 더 줄임

print(end)

