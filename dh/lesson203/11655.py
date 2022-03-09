import sys
S = list(sys.stdin.readline().strip())
for i in S:
    if i.isupper():
        after = ord(i) + 13
        if after>90: after = after - 90 + 64
        print(chr(after), end='')
    elif i.islower():
        after = ord(i) + 13
        if after>122: after = after - 122 + 96
        print(chr(after), end='')
    else:
        print(i, end='')