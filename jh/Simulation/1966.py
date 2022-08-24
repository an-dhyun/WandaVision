# 프린터큐

for i in range(int(input())):
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    location = [0] * N
    location[M] = 1
    count = 0

    while True:
        if array[0] >= max(array):
            count += 1
            if location[0] == 1:
                print(count)
                break
            else:
                del array[0], location[0]
        else:
            array.append(array[0])
            location.append(location[0])
            del array[0], location[0]
