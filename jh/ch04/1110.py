n = int(input())
origin = n
cnt = 0
while True:
    ten = n//10
    one = n%10
    n = 10*one + ((ten+one)%10)
    cnt += 126
    if n == origin:
        break
print(cnt)