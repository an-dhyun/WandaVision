n = int(input())
numbers = list(map(int, str(n)))
numbers.sort(reverse=True)
for i in numbers:
    print(i, end="")