def check(idx):
    p = 0
    for i in range(idx, -1, -1):
        p += result[i]
        if p == 0 and S[i][idx] != 0:
            return False
        elif p < 0 and S[i][idx] >= 0:
            return False
        elif p > 0 and S[i][idx] <= 0:
            return False
    return True

def solve(idx):
    if idx == n: # Base case
        return True
    if S[idx][idx] == 0: # Recursive case
        result[idx] = 0
        return solve(idx+1)
    for i in range(1, 11): # Recursive case
        result[idx] = S[idx][idx] * i
        if check(idx) and solve(idx+1):
            return True
    return False

n = int(input())
arr = list(input())
S = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(i, n):
        temp = arr.pop(0)
        if temp == '+':
            S[i][j] = 1
        elif temp == '-':
            S[i][j] = -1

result = [0] * n
solve(0)
print(' '.join(map(str, result)))