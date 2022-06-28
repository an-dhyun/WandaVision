from ast import Num
import sys
k = int(sys.stdin.readline())
boo = list(sys.stdin.readline().split())

s = []; visited = [False]*10
def dfs(num, depth):
    global max_num
    global min_num
    if len(s)==k+1:
        result = int(''.join(map(str, s)))
        if result>max_num: max_num = result
        if result<min_num:  min_num = result
        return
    if visited[num] == False:
        visited[num] = True
        s.append(num)
        if depth<k and boo[depth]=='>': # 작아져야 할 경우
            if num==0: # 0이면 넘김
                s.pop()
                visited[num] = False
                return 
            else: 
                for i in range(num-1, -1, -1):
                    dfs(i, depth+1)
        elif depth<k and boo[depth]=='<': # 커져야 할 경우
            if num==9: # 9면 넘김
                s.pop()
                visited[num] = False
                return 
            else: 
                for i in range(num+1, 10):
                    dfs(i, depth+1)
        else: # 맨마지막일 경우
            dfs(num, depth+1)
        s.pop()
        visited[num] = False


max_num = 0
min_num = int(1e11)
for i in range(10):
    dfs(i, 0)
print(str(max_num).zfill(k+1)) # 자릿수 맞추기
print(str(min_num).zfill(k+1))