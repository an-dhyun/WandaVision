import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())

maxAnswer = -1e9
minAnswer = 1e9
def dfs(i, result):
    global maxAnswer, minAnswer, add, sub, mul, div
    if i==N:
        if result>maxAnswer: maxAnswer=result
        if result<minAnswer: minAnswer=result
        return
    if add>0:
        add -= 1
        dfs(i+1, result+A[i])
        add += 1
    if sub>0:
        sub -= 1
        dfs(i+1, result-A[i])
        sub += 1
    if mul>0:
        mul -= 1
        dfs(i+1, result*A[i])
        mul += 1
    if div>0:
        div -= 1
        dfs(i+1, int(result/A[i]))
        div += 1

dfs(1, A[0])
print(maxAnswer)
print(minAnswer)

