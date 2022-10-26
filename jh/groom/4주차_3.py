n = int(input())
arr = [1] * 5
for i in range(n-1):
	a, b, c, d, e = arr[0], arr[1], arr[2], arr[3], arr[4]
	arr[0] = (a+b+c+d+e) % 100000007
	arr[1] = (a+c+d)  % 100000007
	arr[2] = (a+b+d)  % 100000007
	arr[3] = (a+b+c+e) % 100000007
	arr[4] = (a+d) % 100000007
print(sum(arr)%100000007)