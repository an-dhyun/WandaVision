N = int(input())
weights = []
heights = []
ranks = [1]*N

for i in range(N):
    w, h = map(int, input().split())
    weights.append(w)
    heights.append(h)
    
for i in range(len(weights)):
    for j in range(len(weights)):
        if heights[i]<heights[j] and weights[i]<weights[j]: ranks[i] += 1

for i in ranks: print(i, end=' ')