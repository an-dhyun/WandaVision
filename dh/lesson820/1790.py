# import sys
# N, k = map(int, sys.stdin.readline().split())
# idx = 0

# while True:
#     if k - (idx+1) * 9 * (10**idx) < 0: break # idx째 자릿수이면 멈추기
#     idx += 1

# answer = str(10**idx + k//(idx+1))
# print(answer[k%(idx+1)])

n, k = map(int, input().split())
ans = 0
digit = 1
nine = 9


while k > digit*nine:
    k = k-(digit * nine)
    ans = ans + nine
    digit+=1
    nine = nine*10

ans = (ans+1) + (k-1) // digit

if ans > n:
    print(-1)
else:
    print(str(ans)[(k-1)%digit])