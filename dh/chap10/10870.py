n = int(input())
first = 0
second = 1
if n==0: print(first)
elif n==1: print(second)
else:
    for i in range(n-1):
        answer = first+second
        first = second
        second = answer
    print(answer)