N = int(input())
A = list(map(int, input().split())) # 길이
B = list(map(int, input().split())) # 주유소

answer = B[0] * A[0] # 비용

for i in range(1, N-1):
    if B[i-1] >= B[i]:
        answer += B[i] * A[i]
    else:
        answer += B[i-1] * A[i]
        B[i] = B[i-1]

print(answer)