xs = []
ys = []
for i in range(3):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
    
xs_uni = list(set(xs))
ys_uni = list(set(ys))

print(2*sum(xs_uni)-sum(xs), 2*sum(ys_uni)-sum(ys))