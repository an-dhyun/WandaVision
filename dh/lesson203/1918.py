import sys
mid = sys.stdin.readline().strip()
i = len(mid)-1
while i>0:
    if mid[i] ==')':
        left = mid.find('(')
        i = left-1
    elif mid[i] in ['+','*','-','/']:
        first = mid[i-1]
        second = mid[i+1]
        before = '%s%s%s'%(first, mid[i], second)
        mid.replace(before,'(%s)'%(before))
    i -= 1
print(''.join(mid))
