esm = list(map(int, input().split()))
e, s, m = 0, 0, 0
cnt = 0
for i in range(15*28*19):
    e += 1 ; s += 1; m += 1
    cnt += 1
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1
    if e == esm[0] and s == esm[1] and m == esm[2]:
        break
print(cnt)