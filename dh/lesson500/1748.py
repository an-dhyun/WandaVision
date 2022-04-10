import sys
N = int(sys.stdin.readline())
len_N = len(str(N)) # 입력된 수의 자리수
answer = 0

for i in range(1,len_N):
    answer += 9*(10**(i-1))*i
answer += len_N*(N-10**(len_N-1)+1)

print(answer)