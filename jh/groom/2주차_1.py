t = int(input())
for i in range(t):
	n = int(input())
	v = list(map(int, input().split()))
	a = 0

	v_mean = sum(v)/n
	for j in v:
		if j>=v_mean:
			a += 1

	print(str(a)+'/'+str(n))