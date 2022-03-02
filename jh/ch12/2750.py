n = int(input())
list_num = []
for _ in range(n):
    num = int(input())
    list_num.append(num)

# bubble sort
for i in range(len(list_num)):
    for j in range(i+1, len(list_num)):
        if list_num[i] > list_num[j]:
            list_num[i], list_num[j] = list_num[j], list_num[i]
for k in list_num:
    print(k)