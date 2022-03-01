t = int(input())
for i in range(t):
    r, s = input().split()
    lst = list(s)
    for j in lst:
        print(j*int(r), end="")
    print("")