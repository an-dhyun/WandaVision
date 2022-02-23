import sys
N = int(sys.stdin.readline())
peoples = []
for i in range(N):
    people = list(map(str, sys.stdin.readline().split()))
    peoples.append(people)
peoples.sort(key = lambda x: int(x[0]))
for i in peoples:
    for j in i:
        print(j, end=' ')
    print()