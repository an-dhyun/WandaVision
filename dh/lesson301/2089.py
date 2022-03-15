import sys
inp = int(sys.stdin.readline())
if inp==0: print(0)
result = ''
while inp:
    if inp % -2 == 0:
        result = str(0) + result
        inp = inp // -2 
    else:
        result = str(1) + result
        inp = inp // -2 + 1
print(result)