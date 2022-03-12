import sys

from django.urls import get_mod_func
A, B = map(int, sys.stdin.readline().split())
to = min(A, B)
gmd = 1; lcm = 1
for num in range(2, to):
    while (A%num==0) & (B%num==0):
        print(num, A, B)
        gmd *= num
        lcm *= num
        A = int(A//num)
        B = int(B//num)
lcm *= A*B
print(gmd); print(lcm)