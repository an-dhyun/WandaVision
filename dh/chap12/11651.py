import sys
N = int(sys.stdin.readline())
places = []
for i in range(N):
    place = list(map(int, sys.stdin.readline().split()))
    places.append(place)
places.sort(key = lambda x : (x[1], x[0]))
for i in places:
    for j in i:
        print(j, end=' ')
    print()