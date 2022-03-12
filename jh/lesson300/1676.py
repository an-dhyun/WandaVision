n = int(input())

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

result = list(map(int,str(factorial(n))))
cnt = 0
for i in range(len(result)):
    if result[-i-1] == 0:
        cnt += 1
    else:
        break
print(cnt)