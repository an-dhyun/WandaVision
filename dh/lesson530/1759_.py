import sys
L, C = map(int, sys.stdin.readline().split())
l = list(sys.stdin.readline().split())
l.sort()

# def check(i): # 모음인지 확인
#     if i in ['a', 'e', 'i', 'o', 'u']: return True
#     else: return False
# def cnt(lst): # 리스트의 모음 개수 확인
#     sum = 0
#     for i in lst: sum += check(i)
#     return sum

# def srh(i):
#     if len(result)>0:
#         res_len = len(result); res_cnt = cnt(result)
#         if res_cnt>=1:
#             if res_len-res_cnt>=L-1: # 완성된 경우
#                 print(*result)
#             else: # 모음 충분, 자음 부족
#                 if        

# result = []
# for i in range(len(l)):
#     srh(i)

s = []; check = [False]*C
def dfs(n):
    if len(s)==L: # 길이가 되면
        c1 = 0; c2 = 0
        for i in s:
            if i in 'aeiou': c1 += 1
            else: c2 += 1
        if c1>=1 and c2>=2:
            print(''.join(s))
        return
    for i in range(n, C):
        if check[i]==False:
            check[i] = True
            s.append(l[i])
            dfs(i)
            s.pop()
            check[i] = False

dfs(0)
