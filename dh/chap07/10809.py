S = input()
S = list(map(str, S))
for i in range(97, 123):
    alp = chr(i)
    place = -1
    if alp in S: place = S.index(alp)
    print(place, end=' ')