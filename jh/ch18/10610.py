N=list(input())
N.sort(reverse=True)
N = int("".join(N))
if N%30==0:
    print(N)
else:
    print(-1)