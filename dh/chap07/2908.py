A, B = map(int, input().split())
A = list(map(str, str(A)))[::-1]
B = list(map(str, str(B)))[::-1]
print(A, B)
A = int("".join(A))
B = int("".join(B))
print(max(A, B))