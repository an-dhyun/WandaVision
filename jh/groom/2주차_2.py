n = int(input())
s = list(input())
answer = 1
for i in range(n-1):
	if s[i] != s[i+1]:
		answer += 1
print(answer)