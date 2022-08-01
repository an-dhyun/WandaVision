N = int(input())
A = [int(input()) for _ in range(N)]
A.sort(reverse=True)
for i in range(0, N):
    A[i] = A[i] * (i+1)

print(max(A))