N = int(input())
input_array = list(map(int, input().split()))

for i in range(N - 1, 0, -1): 
    if input_array[i - 1] < input_array[i]: # 뒷부분이 정렬이 안되어있는 상태라면
        for j in range(N - 1, 0, -1):
            if input_array[i - 1] < input_array[j]:
                input_array[i - 1], input_array[j] = input_array[j], input_array[i - 1]
                input_array = input_array[:i] + sorted(input_array[i:])
                print(*input_array)
                exit() 

print(-1)