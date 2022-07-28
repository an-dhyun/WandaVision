N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True, key=lambda x: x)
answer = 0
for i in range(len(A)):
    answer += A[i]*(i+1)

print(answer)