import sys
age_name = []
n = int(input())
for _ in range(n):
    age_name.append(sys.stdin.readline().split())
age_name.sort(key=lambda x: int(x[0]))
for i in age_name:
    print(i[0], i[1])