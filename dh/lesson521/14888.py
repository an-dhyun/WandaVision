import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().rstrip().split()))
add, sub, mul, div = list(map(int, sys.stdin.readline().rstrip().split()))

maxAnswer = -1e9
minAnswer = 1e9
def dfs(i, result):
    global maxAnswer, minAnswer, add, sub, mul, div
    if i==N:
        if result>maxAnswer: maxAnswer = result
        if result<minAnswer: minAnswer = result
        return
    else:
        if add>0: # 더하기
            add -= 1
            dfs(i+1, result+A[i])
            add += 1 # 바본가
        if sub>0: # 빼기
            sub -= 1
            dfs(i+1, result-A[i])
            sub += 1
        if mul>0: # 곱하기
            mul -= 1
            dfs(i+1, result*A[i])
            mul += 1
        if div>0: # 나누기
            div -= 1
            dfs(i+1, int(result/A[i])) # int하면 버림 -> 음수를 양수로 나눌 때 -0.XX형태가 되면 0으로 만들어줌
            div += 1
dfs(1, A[0])

print(maxAnswer)
print(minAnswer)
