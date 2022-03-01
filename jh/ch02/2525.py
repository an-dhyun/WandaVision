a, b = map(int, input().split())
c = int(input())
if (a+((b+c)//60) < 24) & (b+c>=60):
    print(a+((b+c)//60), (b+c)%60)
elif (a+((b+c)//60) >= 24) & (b+c>=60):
    print((a+((b+c)//60))-24, (b+c)%60)
else:
    print(a, b+c)