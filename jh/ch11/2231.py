n = int(input())
m = 0
for i in range(n+1):
    str_m = list(map(int, str(i)))
    result = i + sum(str_m)
    if result == n:
        print(i)
        break
    if i == n:
        print(0)