import sys
places = []
N = int(sys.stdin.readline())
for i in range(N):
    place = list(map(int, sys.stdin.readline().split()))
    places.append(place)
places.sort(key = lambda x: (x[0], x[1]))

for i in places:
    for j in i:
        print(j, end=' ')
    print()