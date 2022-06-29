import sys
M = int(sys.stdin.readline())
S = set()

def add(n): 
    if n not in S: S.add(n)
def remove(n): 
    if n in S: S.remove(n)
def check(n): 
    if n in S: print(1)
    else: print(0)
def toggle(n):
    if n in S: S.remove(n)
    else: S.add(n)
def all():
    global S
    S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
def empty():
    global S
    S = set()

for _ in range(M):
    coms = list(sys.stdin.readline().split())
    if coms[0]=='add': add(int(coms[1]))
    elif coms[0]=='remove': remove(int(coms[1]))
    elif coms[0]=='check': check(int(coms[1]))
    elif coms[0]=='remove': remove(int(coms[1]))
    elif coms[0]=='toggle': toggle(int(coms[1]))
    elif coms[0]=='all': all()
    elif coms[0]=='empty': empty()
