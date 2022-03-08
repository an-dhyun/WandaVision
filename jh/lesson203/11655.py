import sys
input = sys.stdin.readline

s = list(input().rstrip('\n'))
for i in range(len(s)):
    if s[i].isupper():
        num = ord(s[i]) + 13
        if num <= 90:
            s[i] = chr(num)
        else:
            s[i] = chr(num-26)
    elif s[i].islower():
        num = ord(s[i]) + 13
        if num <= 122:
            s[i] = chr(num)
        else:
            s[i] = chr(num-26)
print(''.join(s))