n, k = map(int, input().split())
inform = []

# 입력 받기
for i in range(n):
	name, height = list(input().split())
	inform.append([name, float(height)])

# 정렬하기
inform.sort(key=lambda x : (x[0], x[1]))

print(inform[k-1][0], '%.2f' % inform[k-1][1])