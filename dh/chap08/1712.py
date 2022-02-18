A, B, C = map(int, input().split())
if C==B and A!=0: print(-1)
elif A//(C-B)>=0: print(A//(C-B)+1)
else: print(-1)
